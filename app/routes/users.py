from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user
from app.extensions import db, login_manager
from app.models import User

user_routes = Blueprint('users', __name__, url_prefix='/users')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@user_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle JSON request
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
        else:
            # Handle form-based submission (fallback for non-AJAX requests)
            username = request.form.get('username')
            password = request.form.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'User already exists'}), 400

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully!'}), 201

    # Render the signup form for GET requests
    return render_template('signup.html')


from flask import request, jsonify

@user_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            # Handle JSON-based request (AJAX)
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
        else:
            # Handle form-based request (traditional form submit)
            username = request.form.get('username')
            password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            if request.is_json:
                return jsonify({'error': 'Invalid credentials'}), 401
            flash('Invalid credentials', 'danger')
            return redirect(url_for('users.login'))

        login_user(user)

        if request.is_json:
            return jsonify({'message': f'Welcome {user.username}!', 'redirect_url': url_for('tasks.get_tasks')}), 200
        
        flash(f'Welcome {user.username}!', 'success')
        return redirect(url_for('tasks.get_tasks'))

    return render_template("login.html")


@user_routes.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('global.home'))