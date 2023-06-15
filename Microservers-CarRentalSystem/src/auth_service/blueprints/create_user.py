import json
import jwt
import requests
from datetime import  datetime,timedelta
from quart import Blueprint, Response, request
from .models.user_model import UserModel
from .models.user_token import Usertoken
from peewee import DoesNotExist
import os
okta_url = os.environ["AUTH_APP_OKTA_BASE_URL"] 

app_scret_key = os.environ["AUTH_SECRET_KEY"]


def generate_access_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(minutes=15), 
        'iat': datetime.utcnow()
    }
    access_token = jwt.encode(payload, app_scret_key, algorithm='HS256')
    return access_token


def generate_refresh_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=30),
        'iat': datetime.utcnow() 
    }
    refresh_token = jwt.encode(payload, app_scret_key, algorithm='HS256')
    return refresh_token

post_user_details_from_api = Blueprint('user_details_from_api', __name__, )

def user_details_token(access_token):
    headers = {
        "Authorization": "Bearer " + access_token,
        "Accept": "application/json"
    }

    userinfo_url = f"https://{okta_url}/oauth2/default/v1/userinfo"  
    response = requests.get(userinfo_url, headers=headers)
    print(response)
    if response.status_code == 200:
        user_details = response.json()
        return user_details
    else:
        print("Error retrieving user details:", response.text)
        return False


@post_user_details_from_api.route('/api/v1/create_user/', methods=['POST'])
async def user_details_from_api() -> Response:
    url = "http://auth_service:8000/callback/"
    print(app_scret_key,"@!###########################$R%^&&&&&&&&&&&&&&&&&&&&&&&&&&")
    token = await request.get_json()
    token = token["accessToken"]
    user_details=user_details_token(access_token=token)
    if not user_details:
        return Response(
                status=403,
                content_type='application/json',
                response=json.dumps({
                    'errors': ['Something is wrong.']
                })
            )
    okta_id = user_details.get("sub")
    email = user_details.get("email")
    first_name = user_details.get("given_name")
    last_name = user_details.get("family_name")
    email_verfied = user_details.get("email_verified")
    zone = user_details.get("zoneinfo")
    try:
        user = UserModel.select().where(UserModel.email == email).get()
    except DoesNotExist :
        new_user = UserModel.create(
        email=email,
        first_name = first_name,
        last_name = last_name,
        username = email,
        email_verfied = email_verfied,
        is_active = True,
        created_at = datetime.now(),
        last_login = datetime.now(),
        okta_id = okta_id,
        zone = zone
        )
        user_token = Usertoken.get_or_create(user=int(new_user.id))
        user_token
        get_user = Usertoken.get(user=int(new_user.id))
        access_token = generate_access_token(int(new_user.id))
        refresh_token = generate_refresh_token(int(new_user.id))
        get_user.access_token=access_token
        get_user.refresh_token=refresh_token
        get_user.save()
        return Response(
            status=201,
            content_type='application/json',
            response=json.dumps({
                
            "message": ['User created successful.'],
            "access token": access_token,
            "refresh token": refresh_token,
            "role": new_user.role}),
            
            )
    except Exception as f:
        return Response(
            status=401,
            content_type='application/json',
            response=json.dumps({
                'Error': [f'{f}']})
            )
    else:
        user.last_login = first_name
        user.token = token
        user.update_at = datetime.now()
        # user.created_at = datetime.now()
        user.last_login = datetime.now()
        # user.role = "admin"
        user.zone = zone
        user.save()
        access_token = generate_access_token(user.id)
        refresh_token = generate_refresh_token(user.id)
        qry = Usertoken.update({Usertoken.access_token:access_token,Usertoken.refresh_token:refresh_token}).where(Usertoken.user==user.id)
        print (qry.sql())
        qry.execute()
        print(refresh_token)

        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps({
                'message': ['user updated successful.'],
                 "access token": access_token,
                "refresh token": refresh_token,
                "role": user.role}),
            )


def verify_jwt_token(token, app_scret_key):
    try:
        # Verify the token's signature and expiration time
        payload = jwt.decode(token, app_scret_key, algorithms=['HS256'])
        
        # Perform additional validations if required
        
        return True, payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return False, None
    except jwt.InvalidTokenError:
        return False, None


def get_user_detail(token):
    is_valid, payload = verify_jwt_token("token", app_scret_key)

    if is_valid:
        user_detail = {}
        user_id = payload.get("user_id")
        username = payload.get("username")
        print(f"User ID: {user_id}")
        print(f"Username: {username}")
        print(payload)
        try:
            user = UserModel.get(UserModel.id == user_id)
            user_detail["username"] = user.username
            user_detail['email'] = user.email
            return user_detail
        except DoesNotExist:
            return None
    else:
        return "Tokne is expired"
        