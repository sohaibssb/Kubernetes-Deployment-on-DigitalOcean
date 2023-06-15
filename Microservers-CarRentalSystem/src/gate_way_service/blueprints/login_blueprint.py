import os
import json
import datetime

from quart import Blueprint, Response, request
from .service_requests import post_data_from_service, delete_data_from_service
from .auth_handler import token_required


login_blurprint = Blueprint('login', __name__, )



def validate_body(body):
    try:
        body = json.loads(body)
    except:
        return None, ['Can\'t deserialize body!']

    errors = []
    if 'accessToken' not in body and 'refreshToken' not in body:
        return None, ['Bad structure body!']

    return body, errors


@login_blurprint.route('/api/v1/login/', methods=['POST'])
async def login() -> Response:    
    body, errors = validate_body(await request.body)
    if len(errors) > 0:
        return Response(
            status=400,
            content_type='application/json',
            response=json.dumps(errors)
        )

    
    response = post_data_from_service(
        'http://' + os.environ['AUTH_SERVICE_HOST'] + ':' + os.environ['AUTH_SERVICE_PORT']
        + '/api/v1/create_user', timeout=5, data=body)
    
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