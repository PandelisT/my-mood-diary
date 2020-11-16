from main import ma
from models.User import User
from marshmallow.validate import Length, Email

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ["password"]

    # add validation for user input before it goes into the database
    email = ma.String(required=True, validate=[Length(min=4), Email()])
    password = ma.String(required=True, validate=Length(min=6))


user_schema = UserSchema()
users_schema = UserSchema(many=True)