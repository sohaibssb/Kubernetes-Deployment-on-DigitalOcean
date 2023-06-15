from peewee import *
from .base_model import BaseModel
from datetime import datetime

ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

class UserModel(BaseModel):
    id = AutoField(primary_key=True, unique=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = CharField(max_length=100, unique=True)
    username = CharField(max_length=100)
    email_verfied = BooleanField(default=False)
    is_active = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(null=True)
    last_login = DateTimeField(null=True)
    role = CharField(max_length=20,  choices=ROLE_CHOICES, default="user")
    okta_id = CharField(max_length=50)
    zone = CharField(max_length=100)
    def to_dict(self):
        return {
            "id": str(self.id),
            "name": str(self.first_name),
            "email": self.email,
        }

    class Meta:
        db_table = "user"
