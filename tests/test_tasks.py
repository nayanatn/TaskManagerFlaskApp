import unittest
from flask_login import FlaskLoginClient
from app import create_app, db
from app.models import User, Task

class TaskTestCase(unittest.TestCase):
    """Test task-related routes with a real database"""

    def setUp(self):
        """Set up test client and database"""
        self.app = create_app('testing')
        self.app.test_client_class = FlaskLoginClient  # Enable login for tests
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()  # Create tables

            # Create a test user and commit it to the database
            user = User(username='testuser')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        """Clean up after tests to prevent unclosed database warnings"""
        with self.app.app_context():
            db.session.remove()  # Ensure the session is closed
            db.drop_all()  # Drop all tables
            db.engine.dispose()  # Properly close the database connection

    def test_create_task(self):
        """Test creating a task"""
        with self.app.app_context():
            user = User.query.filter_by(username='testuser').first()  # Query the user again
            
        with self.client as client:
            client.post('/users/login', json={
                'username': 'testuser',
                'password': 'password123'
            })  # Log in the test user

            response = client.post('/tasks/create', data={
                'title': 'Test Task',
                'description': 'This is a test task.'
            }, follow_redirects=True)

            self.assertEqual(response.status_code, 200)

            # Check if task exists in the database
            with self.app.app_context():
                task = Task.query.filter_by(title='Test Task').first()
                self.assertIsNotNone(task)
                self.assertEqual(task.description, 'This is a test task.')
                self.assertEqual(task.user_id, user.id)

if __name__ == '__main__':
    unittest.main()