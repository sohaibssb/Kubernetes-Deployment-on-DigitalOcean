from peewee import *
from .base_model import BaseModel
from datetime import datetime
from .user_model import UserModel


class Usertoken(BaseModel):
    id = AutoField(primary_key=True, unique=True)
    access_token = TextField(null = True)
    refresh_token = TextField(null= True)
    is_active = BooleanField(default=False)
    user = ForeignKeyField(UserModel, unique=True,  backref='usermodel')
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "name": str(self.access_token),
        }

    class Meta:
        db_table = "usertoken"
