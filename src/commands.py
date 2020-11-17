from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    # from models.Book import Book
    from models.User import User
    from models.Journal import Journal
    from models.ProfileImage import ProfileImage
    from main import bcrypt
    from faker import Faker
    import random

    faker = Faker()
    users = []

    for i in range(1,6):
        user = User()
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        users.append(user)
        print(user)

    db.session.commit()

    for i in range(1,6):
        profile_image = ProfileImage()
        profile_image.filename = f"String for image {i}"
        profile_image.user_id = random.choice(users).id
        db.session.add(profile_image)

    db.session.commit()   

    for i in range(1, 11):
        journal = Journal()
        journal.journal_entry = faker.catch_phrase()
        journal.user_id_fk = random.choice(users).id
        db.session.add(journal)

    db.session.commit()
    print("Tables seeded")