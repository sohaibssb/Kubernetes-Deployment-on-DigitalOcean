import json
from quart import Blueprint, Response, request
from .models.cars_model import CarsModel
from .models.base_model import pg_db

delete_car_order_blueprint = Blueprint('delete_car_order', __name__, )


@delete_car_order_blueprint.route('/api/v1/cars/<string:carUid>/order', methods=['DELETE'])
async def delete_car_order(carUid: str) -> Response:
    try:
        with pg_db.atomic():
            car = CarsModel.select().where(
                CarsModel.car_uid == carUid
            ).get()

            if car.availability is True:
                return Response(
                    status=403,
                    content_type='application/json',
                    response=json.dumps({
                        'errors': ['Car isn\'t ordered.']
                    })
                )

            car.availability = True
            car.save()

            return Response(
                status=200
            )
    except:
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Uid not found in base.']
            })
        )