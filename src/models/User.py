from main import db
from models.ProfileImage import ProfileImage

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    profile_image = db.relationship("ProfileImage", backref="user", lazy="dynamic")
    journal_entries = db.relationship("Journal", backref="users", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.email}>"