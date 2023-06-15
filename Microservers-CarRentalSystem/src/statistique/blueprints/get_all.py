import json
from datetime import  datetime,timedelta
from quart import Blueprint, Response, request
from .models.statistique_model  import StatistiqueModel
from .models.base_model import pg_db
from peewee  import *

get_all_detail = Blueprint('get_all', __name__, )


@get_all_detail.route('/api/v1/get_all_user/', methods=['GET'])
async def get_all() -> Response:
    print("_______________________________TEST")
    try:
        with pg_db.atomic():
            data = [single_data.to_dict() for single_data in StatistiqueModel.select()]
            print(data)
    except Exception as f:
        print("Error -----------------------", f)
    return  Response(
    status=200,
    content_type='application/json',
    response=json.dumps({
        "data": data
    })
    )

