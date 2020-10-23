import unittest
from main import addition

class TestDummyFunction(unittest.TestCase):
    def test_add(self):   
        self.assertEqual(addition(2,3), 5)