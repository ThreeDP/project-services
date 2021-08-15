from django.test import SimpleTestCase

class SimpleTestLogin(SimpleTestCase):
    def test_login_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
