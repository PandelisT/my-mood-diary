from main import db
from models.ProfileImage import ProfileImage

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    profile_image = db.relationship("ProfileImage", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.email}>"