from flask import Blueprint, render_template, request, redirect

from flask_login import login_required, current_user

from models.models import db, Task

from analytics.analytics import task_analytics

task = Blueprint('task', __name__)


@task.route('/dashboard')
@login_required
def dashboard():

    tasks = Task.query.filter_by(user_id=current_user.id).all()

    analytics = task_analytics(tasks)

    return render_template(
        'dashboard.html',
        tasks=tasks,
        analytics=analytics
    )


@task.route('/add-task', methods=['POST'])
@login_required
def add_task():

    title = request.form['title']

    description = request.form['description']

    priority = request.form['priority']

    status = request.form['status']

    task = Task(
        title=title,
        description=description,
        priority=priority,
        status=status,
        user_id=current_user.id
    )

    db.session.add(task)

    db.session.commit()

    return redirect('/dashboard')


@task.route('/delete-task/<int:id>')
@login_required
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)

    db.session.commit()

    return redirect('/dashboard')