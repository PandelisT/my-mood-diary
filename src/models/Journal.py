from main import db
from models.User import User
from models.Client import Client
from datetime import datetime 
from sqlalchemy import text

# create class and table name for tables in database
class Journal(db.Model):
    __tablename__ = "journal"

    id = db.Column(db.Integer, primary_key=True)
    journal_entry = db.Column(db.String())
    journal_date = db.Column(db.DateTime, default=datetime.now)
    client_id_fk = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)

    @classmethod
    def date_filter(cls, year, month, day, user_id):
        sql_query = text("SELECT * FROM  journal WHERE DATE(journal_date) = ':year-:month-:day' and client_id_fk=':user_id';")
        return  db.engine.execute(sql_query, {"year":year, "month": month, "day": day, "user_id": user_id})

    def __repr__(self):
        return f"<Journal {self.journal_entry}>"