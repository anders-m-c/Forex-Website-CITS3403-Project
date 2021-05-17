from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    num_attempts = db.Column(db.Integer, index=True)
    sessionEnded = db.Column(db.Integer, index=True) #startquiz->set to false(0), finish quiz->set to true(1)
    
    #relationship stuff
    quizzes = db.relationship('Quiz', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_latest_quiz(self):
        quizzes = Quiz.query.filter(Quiz.user_id==self.id).all()
        quiz = None
        for q in quizzes:
            quiz = q
        return quiz

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attemptNumber = db.Column(db.Integer, index=True)
    questionNum = db.Column(db.Integer, index=True)
    result = db.Column(db.Integer, index=True) #result for that quiz (15/20 ->stores 15)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    questions = db.relationship('Question', backref='quiz', lazy='dynamic')
    choices = db.relationship('Answer', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<QuizID: {}, Attempt: {}>'.format(self.id, self.attemptNumber)
        
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
    
    def __repr__(self):
        return '<Question: {}>'.format(self.id)
            
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionNum = db.Column(db.Integer, index=True)
    choice = db.Column(db.String(64), index=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    
    def __repr__(self):
        return '<Answer: {}>'.format(self.id)