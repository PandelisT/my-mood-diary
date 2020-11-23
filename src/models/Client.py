from main import db
from models.User import User

class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    journal_entries = db.relationship("Journal", backref="clients", lazy="dynamic")
    # profile_image = db.relationship("ProfileImage", backref="clients", lazy="dynamic")

    def __repr__(self):
        return f"<Client {self.username}>"