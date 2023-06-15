from quart import Quart
from blueprints.models.statistique_model import StatistiqueModel
from blueprints.get_all import get_all_detail
import asyncio
import json
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from aiokafka.errors import KafkaError
import uuid
import ast


app = Quart(__name__)
app.register_blueprint(get_all_detail)

def create_tables():
    StatistiqueModel.drop_table()
    StatistiqueModel.create_table()


KAFKA_INSTANCE = "kafka:9092"
consumer = None

def create_consumer(loop):
    global consumer
    consumer = AIOKafkaConsumer("paymentData", bootstrap_servers=KAFKA_INSTANCE, loop=loop)

async def consume():
    await consumer.start()
    try:
        async for msg in consumer:
            data = ast.literal_eval(msg.value.decode("utf-8"))
            StatistiqueModel.create(
                username=data['username'],
                carID = data['carID'],
                price = data['price'],
                paymentID = data['paymentUid'],
                paymentStatus = data['status']
            )
            
    finally:
        await consumer.stop()


@app.before_serving
async def startup_event():
    loop = asyncio.get_event_loop()
    create_consumer(loop)
    loop.create_task(consume())


@app.after_serving
async def shutdown_event():
    await consumer.stop()


@app.get("/")
def read_root():
    return {"Ping": "Pong"}


if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0',port=8040)
