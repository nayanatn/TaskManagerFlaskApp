# Task Manager

A web-based task management application built with Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-Bcrypt, Jinja2 templates, and AJAX for dynamic interactions.

## Features

- **User Authentication** – Signup, login, and logout with Flask-Login and Flask-Bcrypt.
- **Task Management** – Create, update, delete, and view tasks.
- **AJAX Integration** – Improve user experience with dynamic updates.
- **Jinja2 Templating** – Modular and reusable frontend with HTML templates.
- **Database Migrations** – Flask-Migrate for managing database schema changes.
- **Error Handling** – Custom error pages for better UX.

## Project Structure

```
task_manager/
│── migrations/        # Database migration scripts
│── instance/          # Instance-specific files (e.g., database)
│── app/               # Main application folder
│   │── __init__.py    # Initialize Flask app, Flask-Login
│   │── config.py      # Configuration file (SECRET_KEY, DB settings)
│   │── extensions.py  # Initialize Flask-Login, Flask-Bcrypt, and DB
│   │── models.py      # Database models (User, Task)
│   ├── routes/        # Application routes (Blueprints)
│   │   │── __init__.py  # Register blueprints
│   │   │── global.py    # Home route
│   │   │── users.py     # Signup, Login, Logout with Flask-Login
│   │   │── tasks.py     # Task CRUD operations (protected with @login_required)
│   ├── static/        # Static files (CSS, JS)
│   │   ├── css/       # CSS files
│   │   │   ├── style.css  # Main stylesheet
│   │   ├── js/        # JavaScript files
│   │   │   ├── main.js    # JavaScript for AJAX & UI interactions
│   ├── templates/     # HTML templates
│   │   ├── layout/    # Layout templates
│   │   │   ├── header.html  # Header section
│   │   │   ├── footer.html  # Footer section
│   │   │   ├── base.html    # Base template (extends header/footer)
│   │   ├── home.html     # Homepage
│   │   ├── dashboard.html  # Dashboard (after login)
│   │   ├── login.html      # Login page
│   │   ├── register.html   # Signup page
│   │   ├── errors/         # Error templates
│   │   │   ├── 404.html    # 404 Not Found
│   │   │   ├── 500.html    # 500 Internal Server Error
│   │   ├── tasks/          # Task-related templates
│   │   │   ├── task_list.html  # View all tasks
│   │   │   ├── task_view.html  # View single task details
│   │   │   ├── task_edit.html  # Edit task page
│── run.py             # Entry point to run the Flask app
│── requirements.txt   # List of dependencies
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scriptsctivate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Run the application**

   ```bash
   flask run
   ```

6. **Access the app in your browser**
   ```
   http://127.0.0.1:5000/
   ```

## Environment Variables

Create a `.env` file and add the following:

```ini
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
```

## License

This project is licensed under the MIT License.

---
