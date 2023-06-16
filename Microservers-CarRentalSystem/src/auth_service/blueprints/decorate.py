import jwt
import os

from flask import Flask
from functools import wraps
from datetime import datetime
from quart import Blueprint, Response, request, jsonify



app_scret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None
        if 'access_token' in request.headers:
            token = request.headers['access_token']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            decoded_token = jwt.decode(token, app_scret_key, algorithms=['HS256'])
            
            # user_id = decoded_token.user_id
            expiration_time = decoded_token.get('exp')

            current_time = datetime.utcnow().timestamp()

            if expiration_time and expiration_time < current_time:
                print("Token has expired.")
            else:
                print("Token is still valid.")
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(token, *args, **kwargs)
  
    return decorated