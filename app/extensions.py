from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

# Set the login view
login_manager.login_view = "users.login"  
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "warning"