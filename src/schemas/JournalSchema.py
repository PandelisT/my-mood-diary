from main import ma
from models.Journal import Journal

class JournalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Journal

journal_schema = JournalSchema()
journals_schema = JournalSchema(many=True)