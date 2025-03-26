import unittest
from app import create_app, db
from app.models import User

class AuthTestCase(unittest.TestCase):
    """Test user authentication routes with a real database"""

    def setUp(self):
        """Set up test client and in-memory database"""
        self.app = create_app('testing')  # Use test config
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        # Create a fresh database for testing
        db.create_all()

    def tearDown(self):
        """Clean up after each test"""
        db.session.remove()
        db.drop_all()  # Drop tables to ensure clean state
        self.app_context.pop()

    def test_signup(self):
        """Test user registration with real DB"""
        response = self.client.post('/users/signup', json={
            'username': 'testuser',
            'password': 'password123'
        })

        self.assertEqual(response.status_code, 201)
        self.assertIn(b'User registered successfully', response.data)

        # Check if the user was actually added to the DB
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password('password123'))

    def test_login(self):
        """Test user login with real DB"""
        # Create a test user in the DB
        user = User(username='testuser')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/users/login', json={
            'username': 'testuser',
            'password': 'password123'
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

if __name__ == '__main__':
    unittest.main()