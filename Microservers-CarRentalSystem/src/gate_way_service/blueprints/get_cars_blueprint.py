import os
import json

from quart import Blueprint, Response, request
from .service_requests import get_data_from_service
from .auth_handler import token_required


get_cars_blueprint = Blueprint('get_cars', __name__, )
get_singel_car_blueprint =  Blueprint('get_single_car', __name__, )


@get_cars_blueprint.route('/api/v1/cars/', methods=['GET'])
@token_required
async def get_cars(data, *args, **kwargs) -> Response:
    response = get_data_from_service('http://' + os.environ['CARS_SERVICE_HOST'] + ':' +
                                     os.environ['CARS_SERVICE_PORT'] + '/' + 'api/v1/cars?' +
                                     request.full_path.split('?')[-1], timeout=5)
    if response:
        return Response(
            status=response.status_code,
            content_type='application/json',
            response=response.text
        )
    else:
        return Response(
            status=500,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Cars service is unavailable.']
            })
        )


@get_cars_blueprint.route('/api/v1/car/<string:carUid>', methods=['GET'])
@token_required
async def get_single_car(data, *args, **kwargs):

    carUid = kwargs.get('carUid')
    response = get_data_from_service('http://' + os.environ['CARS_SERVICE_HOST'] + ':' +
                                     os.environ['CARS_SERVICE_PORT'] + '/api/v1/car/'+carUid, timeout=5)
    if response:
        return Response(
            status=response.status_code,
            content_type='application/json',
            response=response.text
        )
    else:
        return Response(
            status=500,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Cars service is unavailable.']
            })
        )