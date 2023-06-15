import os
import json
import datetime

from quart import Blueprint, Response, request
from .service_requests import get_data_from_service
from .auth_handler import admin_user


get_statistique_blurprint = Blueprint('get_all_user', __name__, )



@get_statistique_blurprint.route('/api/v1/get_all/', methods=['GET'])
@admin_user
async def get_all_user(data, *arg, **kwargs ) -> Response: 

    response = get_data_from_service(
        'http://' + os.environ['STATISTIQUE_SERVICE_HOST'] + ':' + os.environ['STATISTIQUE_SERVICE_PORT']
        + '/api/v1/get_all_user/', timeout=5)
    if response is None:
        return Response(
            status=500,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Authentication service is unavailable.']
            })
        )
    return Response(
        status=200,
        content_type='application/json',
        response=json.dumps(response.json())
    )