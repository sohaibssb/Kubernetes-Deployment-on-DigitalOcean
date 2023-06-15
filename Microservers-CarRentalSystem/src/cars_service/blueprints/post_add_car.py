import json
import uuid
from quart import Blueprint, Response, request
from .models.cars_model import CarsModel
from .models.base_model import pg_db
from peewee import DoesNotExist, _transaction

post_cars_blueprint = Blueprint('add_cars', __name__, )


def validate_args(payload):
    errors = []
    brand = payload.get('brand')
    registration_number = payload.get('registration_number')
    model = payload.get('model')
    power = payload.get('power')
    price = payload.get('price')
    availability = payload.get('availability')
    vehicle_type = payload.get('type')

    # Perform validation checks
    if not brand:
        errors.append('Missing brand')
    if not registration_number:
        errors.append('Missing registration number')
    if not model:
        errors.append('Missing model')
    if not power:
        errors.append('Missing power')
    if not price:
        errors.append('Missing price')
    if not vehicle_type:
        errors.append('Missing vehicle type')

    return brand, registration_number, model, power, price, vehicle_type, errors


@post_cars_blueprint.route('/api/v1/add_car_single/', methods=['POST'])
async def add_cars( *args, **kwargs) -> Response:

    payload = await request.json
    brand,registration_number, model, power, price, vehicle_type, errors = validate_args(payload)
    print(brand)
    car_uid= uuid.uuid1()
    if len(errors) > 0:
        return Response(
            status=400,
            content_type='application/json',
            response=json.dumps({
                'errors': errors
            })
    )

    try:
        # with pg_db.atomic():
        car = CarsModel.select().where(CarsModel.car_uid == car_uid).get()
        print(car)
    except DoesNotExist :
        CarsModel.create(
        car_uid = car_uid,
        brand = brand,
        model = model,
        registration_number = registration_number,
        power = power,
        price = price,
        availability = True,
        type = vehicle_type
        )
        return Response(
            status=201,
            content_type='application/json',
            response=json.dumps({
                
            "message": ['Car save successful.'],
            # 'car_uid': car_uid  
            })
            )
    except Exception as f:
        return Response(
            status=401,
            content_type='application/json',
            response=json.dumps({
                'Error': [f'{f}']})
            )
