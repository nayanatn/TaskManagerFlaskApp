from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Task

task_routes = Blueprint('tasks', __name__, url_prefix='/tasks')

@task_routes.route('/')
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("tasks/task_list.html", tasks=tasks)

@task_routes.route('/create', methods=['GET', 'POST'])
@login_required
def create_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        if not title or not description:
            flash("Title and description are required", "danger")
            return redirect(url_for("tasks.create_task"))

        new_task = Task(title=title, description=description, status='pending', user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash("Task created successfully!", "success")
        return redirect(url_for("tasks.get_tasks"))

    return render_template("tasks/task_create.html")

@task_routes.route("/<int:task_id>/edit", methods=['GET', 'POST'])
@login_required
def update_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        flash("Task not found", "danger")
        return redirect(url_for("tasks.get_tasks"))

    if request.method == 'POST':
        task.title = request.form.get('title', task.title)
        task.description = request.form.get('description', task.description)
        new_status = request.form.get('status')

        if new_status:
            try:
                task.set_status(new_status)
            except ValueError:
                flash("Invalid status", "danger")
                return redirect(url_for("tasks.update_task", task_id=task.id))

        db.session.commit()
        flash("Task updated successfully!", "success")
        return redirect(url_for("tasks.get_tasks"))

    return render_template("tasks/task_edit.html", task=task)

@task_routes.route("/<int:task_id>/delete", methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        flash("Task not found", "danger")
        return redirect(url_for("tasks.get_tasks"))

    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!", "success")
    return redirect(url_for("tasks.get_tasks"))