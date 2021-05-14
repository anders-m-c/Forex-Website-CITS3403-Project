from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, QuizForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Quiz, Question, Answer
from werkzeug.urls import url_parse
from app.controllers import UserController, QuizController, QuestionController
import populate_database
from sqlalchemy import and_

@app.route('/')
@app.route('/index')
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
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, \
                    username=form.username.data, email=form.email.data, num_attempts=0, sessionEnded=1)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        msg = "Congratulations {}, you are now a registered user!".format(form.firstname.data)
        flash(msg)
        return redirect(url_for('signin'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/learn', methods=['GET', 'POST'])
def learn():
    return render_template('learn.html', title='Learn')

@app.route('/quiz/<int:id>', methods=['GET', 'POST'])
def quiz(id):
    print("new qnum: ", id)
    if not current_user.is_authenticated:
        flash('You must log in to view the quiz.')
        return redirect(url_for('signin'))
    
    numQuestions = QuestionController.get_number_of_questions()
    attemptNum = current_user.num_attempts
    #if it is not the start of a new quiz - get the user to their last saved question
    print("THIS IS THE ATTEMP NUM: ", attemptNum)
    if current_user.sessionEnded == 0:#1 = THEY HAVE FINISHED 0 = THEY ARE IN A CURRENT SESSION
        print("FFS")
        #get the question number that the user was up to in their last session
        questionNum = 0
        quizzes = Quiz.query.all()
        for q in quizzes:
            if q.author.username == current_user.username and q.attemptNumber == attemptNum:
                print("this the questionNum1", q.questionNum)
                questionNum = q.questionNum
                print("question num: {}".format(questionNum))
        id = questionNum
    populate_database.print_quiz()
    print("this is the id ", id)    
    
    #If it is the start of a new quiz - create a new quiz entry in the database
    if id == 1:
        print("CREATING A QUIZ")
        quiz = Quiz(attemptNumber=attemptNum+1, result=0, author=current_user, questionNum=1)
        db.session.add(quiz)
        current_user.num_attempts = attemptNum + 1
        current_user.sessionEnded = 0
        db.session.commit()
        print('ADDED TO DB')
    print("HELLOOOO")
    attemptNum = current_user.num_attempts
    #get the next question
    q = Question.query.get(id)
    if not q:
        return redirect(url_for('results'))
    #
    if request.method == 'POST':
        # quiz = Quiz.query.filter(Quiz.attemptNumber==attemptNum and Quiz.user_id==current_user.id).first()
        
        quiz = Quiz.query.filter(and_(Quiz.attemptNumber==attemptNum, Quiz.user_id==current_user.id)).first()
        # quiz = quiz2
        # for qui in quiz2:
        #     if qui.author.username == current_user.username:
        #         quiz = qui
        
        option = request.form['options']
        print(option)
        
        #make an answer row with the answer etc.
        answer = Answer(questionNum=id, choice=option, author=quiz)
        db.session.add(answer)
        
        
        if option == q.correct_choice:
            quiz.result = quiz.result + 1
        quiz.questionNum = quiz.questionNum + 1
        print("this the questionNum2", quiz.questionNum)
        db.session.commit()
        print("question num: ", id)
        return redirect(url_for('quiz', id=(id+1)))
    return render_template('quiz3.html', q=q, title='Question {}'.format(id), id=id, numQues=numQuestions)


@app.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    questions = Question.query.all()
    return render_template('results.html', title='Results', questions=questions)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
