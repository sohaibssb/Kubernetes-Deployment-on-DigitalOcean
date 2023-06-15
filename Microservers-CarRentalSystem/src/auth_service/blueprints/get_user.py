import json
import jwt
import requests
from datetime import  datetime,timedelta
from quart import Blueprint, Response, request

from peewee import DoesNotExist

from  .decorate import token_required

get_all_users = Blueprint('get_me', __name__, )
@get_all_users.route('/api/v1/user/', methods=['GET'])
@token_required
def get_me(request) -> Response:
    return  Response(
        status=200,
        content_type='application/json',
        response=json.dumps({
            'message': ['user updated successful.']
        })
    )
