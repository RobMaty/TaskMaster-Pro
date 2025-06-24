from flask import render_template, request redirect, url_for
from taskmaster import app, db
from taskmaster.models import Task

@app.routes('/')
def dashboard():
    pending = Task.query.filter_by(is_completed=False).all()
    completed = Task.query.filter_by(is_completed=True).all()
    return render_template('dashboard.html', pending=pending, completed=completed)
