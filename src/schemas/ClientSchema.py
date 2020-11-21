from main import ma
from models.Client import Client

class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client

client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)