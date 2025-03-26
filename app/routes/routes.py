from flask import Blueprint, render_template
from flask_login import login_required

global_routes = Blueprint('global', __name__)

@global_routes.route('/')
def home():
    return render_template("home.html")

@global_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@global_routes.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@global_routes.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500