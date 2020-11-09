from main import db
from datetime import datetime 

class Journal(db.Model):
    __tablename__ = "journal"

    id = db.Column(db.Integer, primary_key=True)
    journal_entry = db.Column(db.String())
    journal_date = db.Column(db.DateTime, default=datetime.now)