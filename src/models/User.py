
from main import db

from models.Client import Client


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    client_id = db.relationship(Client, backref="user", uselist=False)

    def __repr__(self):
        return f"<User {self.email}>"