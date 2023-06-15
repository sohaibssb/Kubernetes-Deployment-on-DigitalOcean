import json
from quart import Blueprint, Response, request
from .models.cars_model import CarsModel
from .models.base_model import pg_db

delete_car_order_blueprint = Blueprint('delete_car_order', __name__, )


@delete_car_order_blueprint.route('/api/v1/car_delete', methods=['DELETE'])
async def delete_car_order() -> Response:
    payload = await request.json
    carUid = payload.get('carUid')
    try:
        with pg_db.atomic():
            car = CarsModel.select().where(
                CarsModel.car_uid == carUid
            ).get()
            if car.availability == False:
                    return Response(
                    status=403,
                    content_type='application/json',
                    response=json.dumps({
                        'errors': ["Car cannot be deleted. Rental confirmed!"]
                    })
                )

            if car.is_active:
                car.is_active = False
                car.save()
                return Response(
                    status=200,
                    content_type='application/json',
                    response=json.dumps({
                        'errors': ['Car is deleted.']
                    })
                )
            else:
                return Response(
                    status=404,
                    content_type='application/json',
                    response=json.dumps({
                        'errors': ['Uid not found in base.']
                    })
                )
    except:
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Uid not found in base.']
            })
        )