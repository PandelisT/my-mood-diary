from main import db
from sqlalchemy.orm import backref

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    client_id = db.relationship("Client", backref="users", uselist=False)
    # client_id = db.relationship("Client", backref=backref("users", uselist=False))

    def __repr__(self):
        return f"<User {self.email}>"