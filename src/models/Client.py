from main import db

class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    profile_image = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    profile_image = db.relationship("ProfileImage", backref="client", lazy="dynamic")
    journal_entries = db.relationship("Journal", backref="client", lazy="dynamic")



    def __repr__(self):
        return f"<Client {self.username}>"