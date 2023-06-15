import json
from datetime import  datetime
from quart import Blueprint, Response, request
from .models.user_model import UserModel
from peewee import DoesNotExist
import os

get_change_user_role = Blueprint('change_role', __name__, )


@get_change_user_role.route('/api/v1/change_role/', methods=['POST'])
async def change_role() -> Response:

    payload = await request.json
    user_id = payload.get('user_id')
    try:
        user = UserModel.select().where(UserModel.id == user_id).get()
    except DoesNotExist :
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                
            "message": ['User not found.'],
            }),
            )
    except Exception as f:
        return Response(
            status=401,
            content_type='application/json',
            response=json.dumps({
                'Error': [f'{f}']})
            )
    else:
        user.updated_at = datetime.now()
        user.role = "admin"
        user.save()
        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps({
                'message': ['user updated as admin role.'],
                "role": user.role}),
            )
