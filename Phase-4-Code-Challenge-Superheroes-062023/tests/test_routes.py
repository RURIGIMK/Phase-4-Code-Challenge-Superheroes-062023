import unittest
import json
from app import create_app, db
from app.models import User, Recipe

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_user(self):
        response = self.client.post('/users', data=json.dumps({
            'username': 'testuser',
            'password': 'password123'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        user = User(username='testuser', password='password123')
        db.session.add(user)
        db.session.commit()
        response = self.client.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
