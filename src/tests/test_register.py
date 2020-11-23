import unittest
from main import create_app, db
from models.Journal import Journal
from models.Client import Client
from models.User import User
from flask_jwt_extended import create_access_token
import random

class TestAuth(unittest.TestCase):
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

    def test_user_register(self):
        response = self.client.post("/auth/register", 
        json = {                                                        
            "email": "test6@test.com",
            "password": "123456"
        })
        self.assertEqual(response.status_code, 200)

        # data = response.get_json()

        # response = self.client.post("/auth/login", 
        # json = { 
        #     "email": "test6@test.com",
        #     "password": "123456"
        # })                    
        # data = response.get_json()
        # self.assertEqual(response.status_code, 200)