from main import ma
from models.Journal import Journal
from schemas.UserSchema import UserSchema
class JournalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Journal
        users = ma.Nested(UserSchema)

journal_schema = JournalSchema()
journals_schema = JournalSchema(many=True)