import unittest
from application.app import app

class test_login(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.client = app.test_client()

    def test_get_page(self):
        request = self.client.get("/login")
        self.assertEqual(request.status_code, 200)
        self.assertIn(b"Login Page",request.data)
        self.assertIn(b"email",request.data)
        self.assertIn(b"password",request.data)