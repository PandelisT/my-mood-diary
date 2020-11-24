from main import db


class ProfileImage(db.Model):
    __tablename__ = "profile_images"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(), nullable=False, unique=True)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)

    def __repr__(self):
        return f"<ProfileImage {self.filename}>"