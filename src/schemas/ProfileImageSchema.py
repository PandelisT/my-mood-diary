from main import db, ma
from schemas.UserSchema import UserSchema
from models.Client import Client
from models.ProfileImage import ProfileImage
from marshmallow.validate import Length

class ProfileImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfileImage

    filename = ma.String(required=True, validate=Length(min=1))

profile_image_schema = ProfileImageSchema()