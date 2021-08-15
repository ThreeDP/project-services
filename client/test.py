from django.test import SimpleTestCase

class SimpleTestClient(SimpleTestCase):
    def test_client_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_profile_status(self):
        response = self.client.get('/client/profile/')
        self.assertEqual(response.status_code, 200)