from flask import Flask
from functools import wraps
# from models.user_token import UserModel, Usertoken
import jwt
import os
from datetime import datetime
from quart import Blueprint, Response, request, jsonify
from  .models.user_model import UserModel
import json

app_scret_key = os.environ["AUTH_SECRET_KEY"]


get_check_tokne = Blueprint('token_check', __name__, )
@get_check_tokne.route('/api/v1/token/', methods=['POST'])
def token_check(*args, **kwargs):

        token = None
        user_id =None
        if 'access_token' in request.headers:
            token = request.headers['access_token']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
        try:
            decoded_token = jwt.decode(token, app_scret_key, algorithms=['HS256'])
            user_id = decoded_token.get('user_id')
            expiration_time = decoded_token.get('exp')

            current_time = datetime.utcnow().timestamp()
            
            if expiration_time and expiration_time < current_time:
                print("Token has expired.")
            else:
                user = UserModel.select().where(UserModel.id == user_id).get()
                return Response(
                    status=200,
                    content_type='application/json',
                    response=json.dumps({
                        'Message': "valid Token",
                        'message' : 'Token is valid !!',
                        "user_id" : user_id,
                        "first_name" : user.first_name,
                        "last_name" : user.last_name,
                        "email": user.username,
                        "role":user.role
                    })
                    )
               
            
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
