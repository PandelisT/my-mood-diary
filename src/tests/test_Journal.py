import unittest
from main import create_app, db
from models.Journal import Journal
from models.Client import Client
from models.User import User
from flask_jwt_extended import create_access_token
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
        journal_entry = random.choice(Journal.query.all())
        print(journal_entry)
        user = User.query.get(journal_entry.client_id_fk)
        print(user)
        access_token = create_access_token(identity=str(user.id))
        print(access_token)

        response = self.client.get("/journal/", headers={ "Authorization": f"Bearer {access_token}"})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_journal_post(self):
        user = random.choice(User.query.all())
        print(user)
        access_token = create_access_token(identity=str(user.id))
        print(access_token)
        response = self.client.post("/journal/", json={"journal_entry": "test entry"}, headers={ "Authorization": f"Bearer {access_token}"})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
    
