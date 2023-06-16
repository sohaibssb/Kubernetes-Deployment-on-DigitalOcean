
import os
from dotenv import load_dotenv
from peewee import Model, PostgresqlDatabase

# Load environment variables from .env file
load_dotenv()

# Get database connection details from environment variables
db_name = os.getenv('DATA_BASE_NAME')
db_user = os.getenv('DATA_BASE_USER')
db_pass = os.getenv('DATA_BASE_PASS')
db_host = os.getenv('DATA_BASE_HOST')
db_port = int(os.getenv('DATA_BASE_PORT'))

# Create a PostgresqlDatabase instance
pg_db = PostgresqlDatabase(db_name, user=db_user, password=db_pass, host=db_host, port=db_port)

class BaseModel(Model):
    class Meta:
        database = pg_db



# import os
# from peewee import Model, PostgresqlDatabase

# pg_db = PostgresqlDatabase(
#     os.getenv('DATA_BASE_NAME'),
#     user=os.getenv('DATA_BASE_USER'),
#     password=os.getenv('DATA_BASE_PASS'),
#     host=os.getenv('DATA_BASE_HOST'),
#     port=int(os.getenv('DATA_BASE_PORT'))
# )
# # port=int(os.getenv('DATA_BASE_PORT'))

# class BaseModel(Model):
#     class Meta:
#         database = pg_db
