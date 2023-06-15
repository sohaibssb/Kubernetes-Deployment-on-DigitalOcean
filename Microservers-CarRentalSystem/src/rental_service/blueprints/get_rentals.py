import json
from quart import Blueprint, Response, request
from .models.rental_model import RentalModel
from urllib.parse import parse_qs


get_rentals_blueprint = Blueprint('get_rentals', __name__,)


@get_rentals_blueprint.route('/api/v1/rental/', methods=['GET'])
async def get_rentals() -> Response:
    payload = await request.json
    
    user = payload.get('email')

    rentals = [rental.to_dict() for rental in RentalModel.select().where(RentalModel.username == user)]

    return  Response(
        status=200,
        content_type='application/json',
        response=json.dumps(rentals)
    )
