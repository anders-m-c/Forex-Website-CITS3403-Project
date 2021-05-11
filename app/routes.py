from flask import render_template, flash, redirect, url_for, request, json
from app import app, db
from app.forms import LoginForm, RegistrationForm, QuizForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Quiz, Question
from werkzeug.urls import url_parse
import json

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('signin'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('signin.html', title='Sign In', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, num_attempts=0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('signin'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/learn', methods=['GET', 'POST'])
def learn():
    return render_template('learn.html', title='Learn')

@app.route('/quiz/<int:id>', methods=['GET', 'POST'])
def quiz(id):
    if not current_user.is_authenticated:
        return redirect(url_for('signin'))
    attemptNum = current_user.num_attempts
    if current_user.sessionEnded == 0: #1 = THEY HAVE FINISHED 0 = THEY ARE IN A CURRENT SESSION
        #get the question number that the user was up to in their last session
        questionNum = 0
        quizzes = Quiz.query.all()
        for q in quizzes:
            if q.author.username == current_user.username and q.attemptNumber == attemptNum:
                questionNum = q.questionNum
                print("question num: {}".format(questionNum))
        id = questionNum
    print("this is the id ", id)    
    if id == 1:
        quiz = Quiz(attemptNumber=attemptNum+1, result=0, author=current_user, questionNum=1)
        current_user.num_attempts = current_user.num_attempts + 1
        current_user.sessionEnded = 0
        db.session.add(quiz)
        db.session.commit
    q = Question.query.get(id)
    if not q:
        return redirect(url_for('results'))
    if request.method == 'POST':
        #idk if this is right
        quiz = Quiz.query.outerjoin(User, User.id==Quiz.user_id).filter(User.num_attempts==Quiz.attemptNumber).first()
        #quiz = Quiz.query.filter_by(attemptNumber=attemptNum).join(User).first()
        option = request.form['options']
        print(option)
        choice = "q{}choice".format(id)
        quiz.choice = option
        print(quiz.choice)
        if option == q.correct_choice:
            quiz.result = quiz.result + 1
        quiz.questionNum = quiz.questionNum + 1
        db.session.commit()
        print(quiz.choice)
        return redirect(url_for('quiz', id=(id+1)))
    return render_template('quiz3.html', q=q, title='Question {}'.format(id), id=id)


@app.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    return render_template('results.html', title='Results')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
