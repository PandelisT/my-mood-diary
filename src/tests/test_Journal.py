  
import unittest
from main import create_app, db
from schemas.UserSchema import user_schema
from models.User import User
from models.Client import Client
from models.Journal import Journal
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import create_access_token
from controllers.journals_controller import journal
from controllers.auth_controller import auth
from controllers.profile_images_controller import profile_images
from controllers.client_controller import clients


import random

class TestJournal(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])
        print("setup ran")

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
        print("teardown ran")

    def test_journal_index(self):
        # journal_entry = random.choice(Journal.query.all())
        # user = User.query.get(journal_entry.client_id_fk)
        # access_token = create_access_token(identity=str(user.id))

        # response = self.client.get("/journal/", headers={ "Authorization": f"Bearer {access_token}"})
        # data = response.get_json()
        # user_fields = user_schema.load(request.json)
        # user_fields["email"] = "test1@test.com"
        # user_fields["password"] = "123456"
        # user = User.query.filter_by(email=user_fields["email"]).first()

        # expiry = timedelta(days=1)
        # access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

        # header = jsonify({'Content-Type': 'application/json', 'Token': access_token})

        # response = self.client.get("/login/", headers=header)

        # journals = Journal.query.filter_by(client_id_fk=user.id).all()

        # data = response.get_json()
        # print(data)

        # self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, list)
        pass
