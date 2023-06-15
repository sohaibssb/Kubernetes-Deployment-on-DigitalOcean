import os
import json

from quart import Blueprint, Response, request
from .service_requests import delete_data_from_service
from .auth_handler import admin_user


delete_car_blueprint = Blueprint('delete_car', __name__, )


@delete_car_blueprint.route('/api/v1/delete_car', methods=['DELETE'])
@admin_user
async def delete_car(data) -> Response:
    payload = await request.json
    data = await request.get_data()
    car_data = data.decode()
    if not payload:
        payload = json.loads(car_data)
    response = delete_data_from_service('http://' + os.environ['CARS_SERVICE_HOST'] + ':' +
                                     os.environ['CARS_SERVICE_PORT'] + '/' + 'api/v1/car_delete', data=payload, timeout=5)

    if response is None:
        
        return Response(
            status=500,
            content_type='application/json',
            response=json.dumps({
                'errors': ['car service is unavailable.']
            })
        )
    elif response.status_code != 200:
        return Response(
            status=response.status_code,
            content_type='application/json',
            response=response.text
        )
    else:
        car_message = response.json()
        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps(car_message)
        )