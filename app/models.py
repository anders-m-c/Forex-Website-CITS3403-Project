from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    #main attributes
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    num_attempts = db.Column(db.Integer, index=True)
    
    #relationship stuff
    quizzes = db.relationship('Quiz', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attemptNumber = db.Column(db.Integer, index=True)
    sessionEnded = db.Column(db.Integer, index=True) #startquiz->set to false(0), finish quiz->set to true(1)
    result = db.Column(db.Integer, index=True) #result for that quiz (15/20 ->stores 15)
    q1choice = db.Column(db.String(64), index=True)
    q2choice = db.Column(db.String(64), index=True)
    q3choice = db.Column(db.String(64), index=True)
    q4choice = db.Column(db.String(64), index=True)
    q5choice = db.Column(db.String(64), index=True)
    q6choice = db.Column(db.String(64), index=True)
    q7choice = db.Column(db.String(64), index=True)
    q8choice = db.Column(db.String(64), index=True)
    q9choice = db.Column(db.String(64), index=True)
    q10choice = db.Column(db.String(64), index=True)
    q11choice = db.Column(db.String(64), index=True)
    q12choice = db.Column(db.String(64), index=True)
    q13choice = db.Column(db.String(64), index=True)
    q14choice = db.Column(db.String(64), index=True)
    q15choice = db.Column(db.String(64), index=True)
    q16choice = db.Column(db.String(64), index=True)
    q17choice = db.Column(db.String(64), index=True)
    q18choice = db.Column(db.String(64), index=True)
    q19choice = db.Column(db.String(64), index=True)
    q20choice = db.Column(db.String(64), index=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    questions = db.relationship('Question', backref='quiz', lazy='dynamic')
    
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
    img = db.Column(db.String(64), index=True)
    
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
