from taskmaster import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(10), default='Medium')
    due_date = db.Column(db.String(20))
    is_completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'Task: {self.title}'