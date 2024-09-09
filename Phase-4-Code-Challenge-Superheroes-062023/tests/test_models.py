import unittest
from app import create_app, db
from app.models import User, Recipe

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)

    def test_recipe_creation(self):
        user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        recipe = Recipe(title='Test Recipe', description='A description', user_id=user.id)
        db.session.add(recipe)
        db.session.commit()
        self.assertEqual(Recipe.query.count(), 1)
