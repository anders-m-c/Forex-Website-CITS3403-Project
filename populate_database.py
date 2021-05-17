import sys
from app import app, db
from app.models import Question, User, Quiz, Answer

def add_questions():
    ques = Question(question="Which of the following lot sizes is the equivalent of 1,000 units of any given currency?",
        correct_choice="Micro Lot",
        choice1="Standard Lot",
        choice2="Mini Lot", 
        choice3="Micro Lot",
        choice4="Nano Lot")
    db.session.add(ques)
    
    ques = Question(question="Consider a Forex account containing $100 USD. Say you were to trade using USD/JPY, which has a current exchange rate of 103.84. How many pips would the price have to move for your account to reach approx. $150 USD?",
        correct_choice="52 pips",
        choice1="39 pips",
        choice2="48 pips", 
        choice3="52 pips",
        choice4="61 pips")
    db.session.add(ques)
    
    ques = Question(question="Assume that we are using a micro lot size (0.01 unit lot size). We will use the AUD/USD pair. The current exchange rate of AUD/USD is 0.77457. Determine the value per pip.",
        correct_choice="0.129 AUD",
        choice1="12.9 AUD",
        choice2="0.129 AUD", 
        choice3="12.9 USD",
        choice4="0.129 USD")
    db.session.add(ques)
    
    ques = Question(question="Assume that we are using a mini lot size (0.1 unit lot size). We will use the GBP/JPY pair. The current exchange rate of GBP/JPY is 151.183. Determine the value per pip in Japanese Yen.",
        correct_choice="100",
        choice1="50",
        choice2="100", 
        choice3="150",
        choice4="200")
    db.session.add(ques)
    
    ques = Question(question="If in a 30-minute trading session, there are 72 candles present on a daily timeframe chart, how many candles would there be if the timeframe was changed to 15-minutes?",
        correct_choice="6912",
        choice1="1728",
        choice2="3456", 
        choice3="5983",
        choice4="6912")
    db.session.add(ques)
    
    ques = Question(question="What type of candle does the following image represent?",
        correct_choice="Bullish",
        choice1="Doji",
        choice2="30-minute Timeframe", 
        choice3="Bullish",
        choice4="15-minute Timeframe",
        img="candle1.png")
    db.session.add(ques)
    
    ques = Question(question="Given that the candle in the figure is a bearish candle, what price is represented by the x?",
        correct_choice="Open Price",
        choice1="High Price",
        choice2="Open Price", 
        choice3="Low Price",
        choice4="Close Price",
        img="candle2.png")
    db.session.add(ques)
    
    ques = Question(question="Identify the following candlestick pattern.",
        correct_choice="Inverted Hammer",
        choice1="Inverted Hammer",
        choice2="Gravestone Doji", 
        choice3="Long-Legged Doji",
        choice4="Hanging Man",
        img="pattern1.png")
    db.session.add(ques)
    
    ques = Question(question="How can the three white soldiers candlestick pattern be easily identified?",
        correct_choice="Three long bullish candles that follow a downtrend",
        choice1="Three long bearish candles that follow a downtrend",
        choice2="Three long bullish candles that follow a uptrend", 
        choice3="Three long bearish candles that follow a uptrend",
        choice4="Three long bullish candles that follow a downtrend")
    db.session.add(ques)
    
    ques = Question(question="What is characteristic of Doji candles?",
        correct_choice="These candles open and close at the same price",
        choice1="These candles open and close at the same price",
        choice2="These candles always open at their lowest price", 
        choice3="These candles have a large thin body",
        choice4="These candles have a large wide body")
    db.session.add(ques)
    
    ques = Question(question="Which of the following is not a Doji candlestick pattern?",
        correct_choice="Butterfly Doji",
        choice1="Gravestone Doji",
        choice2="Dragonfly Doji", 
        choice3="Butterfly Doji",
        choice4="4-Price Doji")
    db.session.add(ques)
    
    ques = Question(question="Identify the following candlestick pattern.",
        correct_choice="Hammer",
        choice1="Hanging Man",
        choice2="Hammer", 
        choice3="Shooting Star",
        choice4="Bearish Engulfing",
        img="pattern2.png")
    db.session.add(ques)
    
    ques = Question(question="Which currency is the base in the currency pair GBP/USD?",
        correct_choice="GBP",
        choice1="GBP",
        choice2="Neither", 
        choice3="Both",
        choice4="USD")
    db.session.add(ques)
    
    ques = Question(question="What is a limit order?",
        correct_choice="An order to buy or sell at a set price and no higher or lower",
        choice1="An order that needs to be filled today",
        choice2="An order to buy or sell at a set price and no higher or lower", 
        choice3="An order to buy a limited number of lots",
        choice4="An order to limit the price to the market price")
    db.session.add(ques)
    
    ques = Question(question="What is a pip?",
        correct_choice="The minimum movement of a currency",
        choice1="A movement in the price of 100 points",
        choice2="A movement in the price that is less than 10 points", 
        choice3="The minimum movement of a currency",
        choice4="A one cent movement in the price of USD")
    db.session.add(ques)
    
    ques = Question(question="When is the Forex market open?",
        correct_choice="5 days a week, 24 hours a day",
        choice1="5 days a week, 12 hours a day",
        choice2="5 days a week, 24 hours a day", 
        choice3="Monday to Tuesday, 24 hours a day",
        choice4="Always open")
    db.session.add(ques)
    
    ques = Question(question="Is an exponential moving average more reactive than a simple moving average?",
        correct_choice="Yes",
        choice1="No",
        choice2="Sometimes", 
        choice3="Yes",
        choice4="Only on certain timeframes")
    db.session.add(ques)
    
    ques = Question(question="What is the most volatile currency pair?",
        correct_choice="GBPNZD",
        choice1="USDCAD",
        choice2="GBPUSD", 
        choice3="GBPNZD",
        choice4="AUDUSD")
    db.session.add(ques)
    
    ques = Question(question="Which trading session has the largest volume?",
        correct_choice="London Session",
        choice1="London Session",
        choice2="New York Session", 
        choice3="Tokyo Session",
        choice4="Sydney Session")
    db.session.add(ques)
    
    ques = Question(question="What time does the London trading session close (AWST)?",
        correct_choice="3pm-12am",
        choice1="5am-2pm",
        choice2="6am-2pm", 
        choice3="7am-4pm",
        choice4="3pm-12am")
    db.session.add(ques)
    
    db.session.commit()
    numQues = 0
    questions = Question.query.all()
    for q in questions:
        numQues += 1
    print('Populated database with {} questions'.format(numQues))
    return

def add_quizzes():
    quiz = Quiz(attemptNumber=1, questionNum=20, result=7)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=1)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=20)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=15)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=14)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=13)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=12)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=11)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=13)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=18)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=8)
    db.session.add(quiz)
    quiz = Quiz(attemptNumber=2, questionNum=20, result=9)
    db.session.add(quiz)
    
    db.session.commit()
    print("Added quizzes")

def remove_questions():
    questions = Question.query.all()
    for q in questions:
        db.session.delete(q)
    
    db.session.commit()
    print("removed questions")
    
def remove_users():
    users = User.query.all()
    for u in users:
        db.session.delete(u)
    db.session.commit()
    print("removed users")

def remove_answers():
    answers = Answer.query.all()
    for a in answers:
        db.session.delete(a)
    db.session.commit()
    print("removed answers")
    
def remove_quizzes():
    quizzes = Quiz.query.all()
    for q in quizzes:
        db.session.delete(q)
    db.session.commit()
    print("removed quizzes")

def print_questions():
    questions = Question.query.all()
    for q in questions:
        print(q.question)
       
def make_user():
    u = User(firstname="NewUser", lastname="NewUser", username="newuser", num_attempts=0, sessionEnded=1)
    db.session.add(u)
    u.set_password('forex')
    db.session.commit()
    print("Made User")
    
def print_results():
    quizzes = Quiz.query.all()
    for q in quizzes:
        print(q.q1choice)
        percent = q.result/20 * 100
        result = "{}: Scored {}/20 | {}%".format(q.author.username, q.result, percent)
        print(result)
        
def print_quiz():
    quizzes = Quiz.query.all()
    print("|","-"*61,"|")
    print("|  USERNAME |         ID | ATTEMPTNUM | QUESTIONUM |     RESULT |")
    print("|","-"*61,"|")
    for q in quizzes:
        row = "|{:>10} | {:>10} | {:>10} | {:>10} | {:>10} |".format(q.author.username, q.id, q.attemptNumber, q.questionNum, q.result)
        print(row)
    print("|","-"*61,"|")
    
def print_answers():
    answers = Answer.query.all()
    print("|","-"*61,"|")
    for a in answers:
        row = "|{:>10} | {:>10} | {:>10} | {:>10} |".format(a.author.author.username, a.id, a.questionNum, a.choice)
        print(row)
    print("|","-"*61,"|")


if __name__=='__main__':
    if len(sys.argv) == 1:
        print('You must pass in an extra paramter: add_questions | print_questions | remove_questions')
    elif sys.argv[1] == "add_questions":
        add_questions()
    elif sys.argv[1] == "print_questions":
        print_questions()
    elif sys.argv[1] == "remove_questions":
        remove_questions()
    elif sys.argv[1] == "make_user":
        make_user()
    elif sys.argv[1] == "print_results":
        print_results()
    elif sys.argv[1] == "remove_users":
        remove_users()
    elif sys.argv[1] == "remove_quizzes":
        remove_quizzes()
    elif sys.argv[1] == "print_quiz":
        print_quiz()
    elif sys.argv[1] == "print_answers":
        print_answers()
    elif sys.argv[1] == "remove_answers":
        remove_answers()
    elif sys.argv[1] == "add_quizzes":
        add_quizzes()    