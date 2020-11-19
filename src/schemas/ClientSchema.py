from main import ma
from models.Client import Client
from marshmallow.validate import Length, Email

class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client

    # add validation for user input before it goes into the database
    # email = ma.String(required=True, validate=[Length(min=4), Email()])
    # password = ma.String(required=True, validate=Length(min=6))


client_schema = UserSchema()
clients_schema = UserSchema(many=True)