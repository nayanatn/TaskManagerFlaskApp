from app.extensions import db, bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #foreign key in Task
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    #relationship to task -> one to many
    tasks = db.relationship('Task',backref='user',lazy=True,cascade='all, delete')

    def set_password(self,password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) #foreign key in Task
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(120))
    status = db.Column(db.String(120), default='pending', nullable=False)

    #foreign key from User model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    
    def set_status(self,new_status):
        if new_status not in ['pending','completed']:
            raise ValueError('Invalid status value')
        self.status = new_status