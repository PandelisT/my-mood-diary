from flask_sqlalchemy import SQLAlchemy
import os

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/my_mood_diary"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app) # new instance of db connection
    return db
