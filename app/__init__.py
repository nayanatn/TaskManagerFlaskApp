from flask import Flask
from flask_login import current_user
from app.config import Config, TestingConfig
from app.extensions import db, migrate, login_manager, bcrypt
from app.routes import register_routes 

def create_app(config_name = 'default'):
    app = Flask(__name__)
    
    if config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(Config)


    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Inject current_user into Jinja templates
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    register_routes(app)

    return app