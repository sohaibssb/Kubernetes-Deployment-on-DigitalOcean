import os
import json

from quart import Blueprint, Response, request
from .service_requests import get_data_from_service
from .auth_handler import token_required

get_rental_blueprint = Blueprint('get_rental', __name__, )


def car_simplify(car: dict) -> dict:
    return {
        "carUid": car['carUid'],
        "brand": car['brand'],
        "model": car['model'],
        "registrationNumber": car['registrationNumber']
    }


@get_rental_blueprint.route('/api/v1/rental/<string:rentalUid>', methods=['GET'])
@token_required
async def get_rental(data, *args, **kwargs) -> Response:
    try:
        username = data.get("email")
        rentalUid = kwargs.get('rentalUid')
        response = get_data_from_service(
            'http://' + os.environ['RENTAL_SERVICE_HOST'] + ':' + os.environ['RENTAL_SERVICE_PORT']
            + '/api/v1/rental/'+rentalUid, timeout=5, headers={'username': username})
        if response is None:
            return Response(
                status=500,
                content_type='application/json',
                response=json.dumps({
                    'errors': ['Rental service is unavailable.']
                })
            )

        rental = response.json()
        response = get_data_from_service(
            'http://' + os.environ['CARS_SERVICE_HOST'] + ':' + os.environ['CARS_SERVICE_PORT']
            + '/api/v1/car/' + rental['carUid'], timeout=5)
        if response is None:
            return Response(
                status=500,
                content_type='application/json',
                response=json.dumps({
                    'errors': ['Car service is unavailable.']
                })
            )
        del rental['carUid']
        rental['car'] =  car_simplify(response.json())

        response = get_data_from_service(
            'http://' + os.environ['PAYMENT_SERVICE_HOST'] + ':' + os.environ['PAYMENT_SERVICE_PORT']
            + '/api/v1/payment/' + rental['paymentUid'], timeout=5)
        if response is None:
            return Response(
                status=500,
                content_type='application/json',
                response=json.dumps({
                    'errors': ['Car service is unavailable.']
                })
            )
        rental['payment'] = response.json()
        del rental['paymentUid']

        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps(rental)
        )
    except Exception as e:
        return Response(
            status=500,
            content_type='application/json',
            response=[f"error {e}"]
        )