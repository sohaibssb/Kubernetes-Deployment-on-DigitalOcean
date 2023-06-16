import uuid
import json
from quart import Blueprint, Response, request
from .models.payment_model import PaymentModel
from aiokafka import AIOKafkaProducer
import asyncio
import os

KAFKA_HOST = "146.190.114.149"
KAFKA_PORT = "9092"
KAFKA_INSTANCE = f"{KAFKA_HOST}:{KAFKA_PORT}"

print(KAFKA_INSTANCE,'////////////////////////////////////666666666666666666666666666')

aioproducer = None

async def start_producer(loop):
    global aioproducer
    aioproducer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_INSTANCE)
    await aioproducer.start()


post_payment_blueprint = Blueprint('post_payment', __name__,)


def validate_body(body):
    try:
        body = json.loads(body)
        print(body,"*****************************************")
    except:
        return None, ['Can\'t deserialize body!']

    errors = []
    if 'price' not in body.keys() or type(body['price']) is not int:
        return None, ['Bad structure body!']

    return body, errors


@post_payment_blueprint.route('/api/v1/payment/', methods=['POST'])
async def post_payment() -> Response:
    body, errors = validate_body(await request.body)
    if len(errors) > 0:
        return Response(
            status=400,
            content_type='application/json',
            response=json.dumps(errors)
        )

    payment = PaymentModel.create(
        payment_uid=uuid.uuid4(),
        price=body['price'],
        status='PAID'
    )

    static_data = payment.to_dict()
    static_data['username'] = body['username']
    static_data['carID'] = body['carUid']

    await aioproducer.send('paymentData', json.dumps(static_data).encode("ascii"))

    return Response(
        status=200,
        content_type='application/json',
        response=json.dumps(payment.to_dict())
    )
