from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    num_logins = db.Column(db.Integer, index=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    results = db.relationship('Quiz', backref='author', lazy='dynamic')
    #questions = db.relationship('Question', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, index=True)
    num_attempts = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    questions = questions = db.relationship('Question', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<Result {}>'.format(self.result)
    
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    correct_choice = db.Column(db.String(64), index=True)
    choice1 = db.Column(db.String(64), index=True)
    choice2 = db.Column(db.String(64), index=True)
    choice3 = db.Column(db.String(64), index=True)
    choice4 = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    img_id = db.relationship('Image', backref='author', lazy='dynamic')
    
    #get_question_images
    
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))