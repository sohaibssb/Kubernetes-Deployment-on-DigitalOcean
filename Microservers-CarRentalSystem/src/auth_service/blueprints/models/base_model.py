import os
from peewee import Model, PostgresqlDatabase


pg_db = PostgresqlDatabase(
    "user_db",
    user="program",
    password="test",
    host="postgres",
    port=5432
)


class BaseModel(Model):
    class Meta:
        database = pg_db
