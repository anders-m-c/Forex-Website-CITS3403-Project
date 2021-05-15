from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, QuizForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Quiz, Question, Answer
from werkzeug.urls import url_parse
from app.controllers import UserController, QuizController, QuestionController
import populate_database
from sqlalchemy import and_

from plotly.offline import plot
from plotly.graph_objs import *
from flask import Markup
import plotly.express as px

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


@app.route('/learn_beginner', methods=['GET', 'POST'])
def learn_beginner():
    return render_template('learn_beginner.html', title='Learn - Beginner')

@app.route('/learn_intermediate', methods=['GET', 'POST'])
def learn_intermediate():
    return render_template('learn_intermediate.html', title='Learn - Intermediate')

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
    print("CURRENT_USER: ", current_user.sessionEnded)
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
        current_user.sessionEnded = 1
        db.session.commit()
        return redirect(url_for('results'))
    filelocation = "images/{}".format(q.img)
    image_file = url_for('static', filename=filelocation)
    if request.method == 'POST':        
        quiz = Quiz.query.filter(and_(Quiz.attemptNumber==attemptNum, Quiz.user_id==current_user.id)).first()
        
        option = request.form['options']
        print(option)
        
        answer = Answer(questionNum=id, choice=option, author=quiz)
        db.session.add(answer)
        if option == q.correct_choice:
            quiz.result = quiz.result + 1
        quiz.questionNum = quiz.questionNum + 1
        print("this the questionNum2", quiz.questionNum)
        db.session.commit()
        print("question num: ", id)
        return redirect(url_for('quiz', id=(id+1)))
    return render_template('quiz3.html', q=q, title='Question {}'.format(id), id=id, numQues=numQuestions, img=image_file)


@app.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    questions = Question.query.all()
    
    plots = []
    
    choices = [0, 0, 0, 0]
    
    # how many choose choice 1... 
    answers = Answer.query.all()
    
    for ques in questions:
        for ans in answers:
            if ans.questionNum == ques.id:
                if ans.choice == ques.choice1:
                    choices[0] = choices[0] + 1
                elif ans.choice == ques.choice2:
                    choices[1] = choices[1] + 1
                elif ans.choice == ques.choice3:
                    choices[2] = choices[2] + 1
                elif ans.choice == ques.choice4:
                    choices[3] = choices[3] + 1
        names = [ques.choice1, ques.choice2, ques.choice3, ques.choice4]
        fig = px.pie(values=choices, names=names, width=300, height=300)
        fig.layout.update(showlegend=False)
        div = fig.to_html(full_html=False)
        plots.append(Markup(div))
        choices = [0, 0, 0, 0]
    
    quiz = Quiz.query.filter(Quiz.attemptNumber==current_user.num_attempts).first()
    print("QUIZZZ: ", quiz.id)
    previous_quiz_answers = Answer.query.filter(Answer.quiz_id==quiz.id).all()
    attempted_questions = len(previous_quiz_answers)
    
    return render_template('results.html', title='Results', questions=questions, div_placeholder=plots, previous_quiz_answers=previous_quiz_answers, attempted_questions=attempted_questions)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/what_is_forex')
def what_is_forex():
    return render_template('content_pages/what_is_forex.html', title='What is Forex')

@app.route('/buying_and_selling')
def buying_and_selling():
    return render_template('content_pages/buying_and_selling.html', title='Buying and Selling')

@app.route('/how_to_make_money')
def how_to_make_money():
    return render_template('content_pages/how_to_make_money.html', title='How to Make Money')

@app.route('/pips')
def pips():
    return render_template('content_pages/pips.html', title='Pips')

@app.route('/lot_sizes')
def lot_sizes():
    return render_template('content_pages/lot_sizes.html', title='Lot Sizes')

@app.route('/types_of_orders')
def types_of_orders():
    return render_template('content_pages/types_of_orders.html', title='Types of Orders')

@app.route('/demo_vs_real')
def demo_vs_real():
    return render_template('content_pages/demo_vs_real.html', title='Demo Vs. Real')

@app.route('/trading_sessions')
def trading_sessions():
    return render_template('content_pages/trading_sessions.html', title='Trading Sessions')

@app.route('/candles')
def candles():
    return render_template('content_pages/candles.html', title='Candles')

@app.route('/support_and_resistance')
def support_and_resistance():
    return render_template('content_pages/support_and_resistance.html', title='Support and Resistance')

@app.route('/trends')
def trends():
    return render_template('content_pages/trends.html', title='Trends')

@app.route('/trading_support_and_resistance')
def trading_support_and_resistance():
    return render_template('content_pages/trading_support_and_resistance.html', title='Trading Support and Resistance')

@app.route('/candlestick_patterns')
def candlestick_patterns():
    return render_template('content_pages/candlestick_patterns.html', title='Candlestick Patterns')

@app.route('/moving_averages')
def moving_averages():
    return render_template('content_pages/moving_averages.html', title='Moving Averages')