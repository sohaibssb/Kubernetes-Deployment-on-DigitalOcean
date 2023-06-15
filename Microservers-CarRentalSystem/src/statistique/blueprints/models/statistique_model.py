from peewee import *
from .base_model import BaseModel

class StatistiqueModel(BaseModel):
    id = IdentityField()
    username = CharField(max_length=55)
    carID = CharField(max_length=55)
    price = CharField(max_length=55)
    paymentID = CharField(max_length=55)
    paymentStatus = CharField(max_length=55)

    def to_dict(self):
        return {
            "username": str(self.username),
            "carID": str(self.carID),
            "paymentID": str(self.paymentID),
            "paymentStatus": str(self.paymentStatus),
            "id": str(self.id),
            "price": self.price,
        }

    class Meta:
        db_table = "statistique"
