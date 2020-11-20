from main import ma
from models.Client import Client
from marshmallow.validate import Length, Email

class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client

client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)