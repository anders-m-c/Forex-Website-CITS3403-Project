from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, QuizForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Quiz, Question, Answer
from werkzeug.urls import url_parse
from sqlalchemy import func
from flask import Markup
import plotly.express as px
import pandas as pd

class QuestionController():
    def get_number_questions():
        numQuestions = 0
        questions = Question.query.all()
        for q in questions:
            numQuestions += 1
        return numQuestions

class QuizController():
    #get the total number of attempts from all users
    def get_total_attempts():
        quizzes = Quiz.query.all()
        attempts = 0
        for q in quizzes:
            attempts += 1
        return attempts        
        
    #returns the average result of all attempts of the quiz (mark)
    def get_average_result():
        quizzes = Quiz.query.all()
        result = 0
        for q in quizzes:
            result += q.result
        attempts = QuizController.get_total_attempts()
        return result/attempts
            
    #gets the top 3 quiz attempts and returns them as a list    
    def get_leaderboard():
        top3 = []
        top3_results = []
        all_users_quizzes = User.query.outerjoin(Quiz, User.id==Quiz.user_id).add_columns(User.username, Quiz.result).order_by(Quiz.result.desc()).all()
        index = 0
        if len(all_users_quizzes) >= 3:
            for i in range(3):
                username = all_users_quizzes[i].username
                result = all_users_quizzes[i].result
                top3_user = "{}. {}: {}".format(i+1, username, result)
                top3.append(top3_user)
        return top3
    
    #gets the pass rate of the quiz given all the attempts
    def get_passrate():
        quizzes = Quiz.query.all()
        numQues = QuestionController.get_number_questions()
        numPass = 0
        for q in quizzes:
            if q.result >= (numQues/2):
                numPass += 1
        
        return numPass/QuizController.get_total_attempts() * 100
                
class AnswerController():
    #makes a pie graph for each question based on the number of times
    #each choice has been selected
    def make_piegraphs():
        plots = []
        choices = [0, 0, 0, 0]
        
        answers = Answer.query.all()
        questions = Question.query.all()
        
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
        return plots
    
    #makes a histogram of the results of all students
    def make_histrogram():
        quizzes = Quiz.query.all()
        results = []
        for q in quizzes:
            results.append(q.result)
        
        result_str = "Result of out {}".format(QuestionController.get_number_questions())
        data = {result_str:results}

        df = pd.DataFrame(data)
                
        # df = px.data.tips()
        fig = px.histogram(df, x=result_str, width=550, height = 375)
        div = fig.to_html(full_html=False)
        div2 = Markup(div)
        return div2
                
    
