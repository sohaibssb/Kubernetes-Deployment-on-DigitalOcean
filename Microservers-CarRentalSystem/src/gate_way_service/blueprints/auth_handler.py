from functools import wraps
from datetime import datetime
import requests
from retrying import retry
from functools import wraps
from quart import request, abort, jsonify
import os


@retry(stop_max_attempt_number=3, wait_fixed=1000)
async def decode_token( access_token: str):
    """
        This method is used for decoding access token to get payload data.
    """
    try:
        url = 'http://' + os.environ['AUTH_SERVICE_HOST'] + ':' + os.environ['AUTH_SERVICE_PORT']+ '/api/v1/token'
        headers = {
        'access_token': access_token
        }
        request_obj = requests.post(url, headers=headers, data='', timeout=10)
        data = request_obj.json()
        if request_obj.status_code == 200:
            return True, data
        else:
            return False, []
    except Exception as e:
        return False, []
    



def token_required(f):
    @wraps(f)
    async def decorated_function(*args, **kwargs):
        token = request.headers.get('access_token')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        validate, data = await decode_token(token)
        if not validate:
            return jsonify({'message': 'Invalid Token'}), 401

        return await f(data, *args, **kwargs)

    return decorated_function

def admin_user(f):
    @wraps(f)
    async def decorated_user(*args, **kwargs):
        token = request.headers.get('access_token')
        
        # Perform token validation logic here
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        validate, data = await decode_token(token)
        if not validate:
            return jsonify({'message': 'Invalid Token'}), 401
        
        if data.get("role") != "admin":
            return  jsonify({'message': 'you have not permission.'}), 401

        # Continue with the route handler
        return await f(data, *args, **kwargs)

    return decorated_user