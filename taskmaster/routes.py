from flask import render_template, request redirect, url_for
from taskmaster import app, db
from taskmaster.models import Task

@app.routes('/')
def dashboard():
    pending = Task.query.filter_by(is_completed=False).all()
    completed = Task.query.filter_by(is_completed=True).all()
    return render_template('dashboard.html', pending=pending, completed=completed)

@app.route('/create', methods=['POST'])
def create_task():
    new_task = Task(
        title=request.from.get('title'),
        priority=request.from.get('priority'),
        due_date=request.from.get('due_date'),
        is_completed=False
    )
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('dashboard'))

app.route('/update/int:task_id>')
def update_status(task_id):
    task = Task.query.get_or_404(task_id)
    task.is_completed = not task.is_completed
    db.session.commit()
    return redirect(url_for('dashboard'))