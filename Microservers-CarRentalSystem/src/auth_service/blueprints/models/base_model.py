import os
from peewee import Model, PostgresqlDatabase


pg_db = PostgresqlDatabase(
    os.getenv('DATA_BASE_NAME'),
    user=os.getenv('DATA_BASE_USER'),
    password=os.getenv('DATA_BASE_PASS'),
    host=os.getenv('DATA_BASE_HOST'),
    port=5432
)


class BaseModel(Model):
    class Meta:
        database = pg_db
