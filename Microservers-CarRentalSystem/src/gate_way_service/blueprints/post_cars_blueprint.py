import os
import json
import datetime

from quart import Blueprint, Response, request
from .service_requests import post_data_from_service
from .auth_handler import admin_user


post_car_blueprint = Blueprint('add_car', __name__, )



@post_car_blueprint.route('/api/v1/add_car/', methods=['POST'])
@admin_user
async def add_car(data, *args, **kwargs) -> Response:
    data = await request.get_data()
    car_data = data.decode()
    payload = await request.json
    if payload is None:
        payload =json.loads(car_data)
    response =  post_data_from_service(
        'http://' + os.environ['CARS_SERVICE_HOST'] + ':' +
                                     os.environ['CARS_SERVICE_PORT'] + '/' + 'api/v1/add_car_single/', data=payload, timeout=5)
    print(response.json())
    if response is None:
        return  Response(
            status=500,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Authentication service is unavailable.']
            })
        )
    return  Response(
        status=200,
        content_type='application/json',
        response=json.dumps(response.json())
    )