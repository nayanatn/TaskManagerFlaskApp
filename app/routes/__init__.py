from flask import Blueprint

from .users import user_routes
from .tasks import task_routes
from .routes import global_routes

def register_routes(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(task_routes)
    app.register_blueprint(global_routes)