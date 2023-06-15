import json
import requests

from quart import Blueprint, Response, request


from  .decorate import token_required

post_callback = Blueprint('callback', __name__, )
@post_callback.route('callback/', methods=['POST'])
def callback(request) -> Response:
    return  Response(
        status=200,
        content_type='application/json',
        response=json.dumps({
            'tokne': ['token']
        })
    )
