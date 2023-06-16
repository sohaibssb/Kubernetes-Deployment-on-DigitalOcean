import os
from peewee import Model, PostgresqlDatabase

pg_db = PostgresqlDatabase(
    "cars",
    user="program",
    password="test",
    host="postgres",
    port=5432
)
# port=int(os.getenv('DATA_BASE_PORT'))

class BaseModel(Model):
    class Meta:
        database = pg_db
