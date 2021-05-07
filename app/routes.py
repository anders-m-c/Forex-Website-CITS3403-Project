from flask import render_template, flash, redirect, url_for, request, json
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Quiz, Question
from werkzeug.urls import url_parse
import json

questionNumber = 0

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


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions2 = Question.query.all()
    global questionNumber
    questionNumber += 1
    return render_template('quiz3.html', title='Test Your Knowledge', ques=questions2, qNum=questionNumber)

@app.route('/quiz/previous', methods=['GET', 'POST'])
def previous():
    questions2 = Question.query.all()
    global questionNumber
    questionNumber -= 1
    return render_template('quiz3.html', title='Test Your Knowledge', ques=questions2, qNum=questionNumber)



@app.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    return render_template('results.html', title='Results')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
