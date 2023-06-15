import os
import json
import datetime

from quart import Blueprint, Response, request
from .service_requests import post_data_from_service
from .auth_handler import token_required


post_car_blueprint = Blueprint('change_role', __name__, )

@post_car_blueprint.route('/api/v1/change_role/', methods=['POST'])
@token_required
async def change_role(data, *args, **kwargs) -> Response:
    response =  post_data_from_service(
        'http://' + os.environ['AUTH_SERVICE_HOST'] + ':' + os.environ['AUTH_SERVICE_PORT']+ '/' + 'api/v1/change_role/', data=data, timeout=5)
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