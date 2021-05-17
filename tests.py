import unittest
from app import app, db
from app.models import User, Quiz, Question, Answer
from app.controllers import QuizController, QuestionController

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app = app.test_client()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    #Tests the hashing of the set password function
    def test_password_hashing(self):
        user = User(username='anders')
        user.set_password('mike34')
        
        self.assertFalse(user.check_password('mike35'))
        self.assertTrue(user.check_password('mike34'))
        
    #Test if get_latest_quiz returns the last quiz that user did
    def test_get_latest_quiz(self):
        #User does 2 quizzes
        user = User(username='anders')
        db.session.add(user)
        quiz1 = Quiz(attemptNumber=1, questionNum=20, result=15, author=user)
        quiz2 = Quiz(attemptNumber=2, questionNum=3, result=2, author=user)
        db.session.add(quiz1)
        db.session.add(quiz2)
        db.session.commit()
        
        self.assertEqual(user.get_latest_quiz(), quiz2)
        
        #If they haven't done any quizzes yet
        user2 = User(username="newuser")
        db.session.add(user2)
        db.session.commit()
        self.assertEqual(user2.get_latest_quiz(), None)
        
    #Test is check_choice correctly checks if the user selects the correct option
    # def test_check_choice(self):
    #     user = User(username="anders")
        
    #     quiz = Quiz(attemptNumber=1, questionNum=3, result=2, author=user)
    
    #Test is get_result correctly outputs the result message of a quiz
    # def test_get_result(self):
    #     user = User(username="anders")
    #     quiz = Quiz(attemptNumber=1, questionNum=20, result=18, author=user)
        
    #     percent = 18/20 * 100
    #     result = "You scored: 18 out of 20, achieving {}%".format(percent)
        
    #     self.assertEqual(quiz.get_result(), result)
        
    #Test is get_number_questions correctly outputs the number of questions in the quiz database
    def test_get_number_questions(self):
        user = User(username="anders")
        db.session.add(user)
        quiz = Quiz(attemptNumber=1, questionNum=0, result=0, author=user)
        db.session.add(quiz)
        question1 = Question(question="How are you?")
        db.session.add(question1)
        question2 = Question(question="What are you doing?")
        db.session.add(question2)
        question3 = Question(question="Who are you?")
        db.session.add(question3)
        db.session.commit()
        
        self.assertEqual(QuestionController.get_number_questions(), 3)
        
    #Test is get_total_attempts correctly outputs the number of attempts made by all users
    def test_get_total_attempts(self):
        user = User(username="anders")
        db.session.add(user)
        user2 = User(username="mike")
        db.session.add(user2)
        db.session.commit()
        
        for i in range(100):
            quiz = Quiz(attemptNumber=i, questionNum=0, result=0, author=user)
            db.session.add(quiz)
        for i in range(30):
            quiz = Quiz(attemptNumber=i, questionNum=0, result=0, author=user2)
            db.session.add(quiz)
            
        db.session.commit()
        
        self.assertEqual(QuizController.get_total_attempts(), 130)
        
    def test_get_average_result(self):
        user = User(username="anders")
        db.session.add(user)
        user2 = User(username="mike")
        db.session.add(user2)
        db.session.commit()
        
        quiz = Quiz(attemptNumber=1, questionNum=20, result=12, author=user)
        db.session.add(quiz)
        quiz = Quiz(attemptNumber=1, questionNum=20, result=15, author=user2)
        db.session.add(quiz)
        quiz = Quiz(attemptNumber=1, questionNum=20, result=18, author=user)
        db.session.add(quiz)
        quiz = Quiz(attemptNumber=1, questionNum=20, result=6, author=user2)
        db.session.add(quiz)
        db.session.commit()
        
        expected_average = (12+15+18+6) / 4
            
        self.assertEqual(QuizController.get_average_result(), expected_average)
        
    #Test is get_leaderboard correctly obtains the top 3 users
    def test_get_leaderboard(self):
        user = User(username="newuser1")
        db.session.add(user)
        user2 = User(username="newuser2")
        db.session.add(user2)
        user3 = User(username="newuser3")
        db.session.add(user3)
        user4 = User(username="newuser4")
        db.session.add(user4)
        db.session.commit()
        
        quiz = Quiz(attemptNumber=1, questionNum=20, result=12, author=user)
        db.session.add(quiz)
        quiz = Quiz(attemptNumber=1, questionNum=20, result=15, author=user2)
        db.session.add(quiz)
        quiz = Quiz(attemptNumber=1, questionNum=20, result=18, author=user3)
        db.session.add(quiz)
        quiz = Quiz(attemptNumber=1, questionNum=20, result=6, author=user4)
        db.session.add(quiz)
        db.session.commit()
        
        top3 = []
        first = "1. newuser3: 18"
        second = "2. newuser2: 15"
        third = "3. newuser1: 12"
        top3.append(first)
        top3.append(second)
        top3.append(third)
        
        self.assertEqual(QuizController.get_leaderboard(), top3)
        
    def test_get_passrate(self):
        user = User(username="newuser1")
        db.session.add(user)
        user2 = User(username="newuser2")
        db.session.add(user2)
        user3 = User(username="newuser3")
        db.session.add(user3)
        user4 = User(username="newuser4")
        db.session.add(user4)
        db.session.commit()
        
        question1 = Question(question="How are you?")
        db.session.add(question1)
        question2 = Question(question="What are you doing?")
        db.session.add(question2)
        question3 = Question(question="Who are you?")
        db.session.add(question3)
        question4 = Question(question="What day is it?")
        db.session.add(question4)
        db.session.commit()
        
        quiz = Quiz(attemptNumber=1, questionNum=20, result=3, author=user)
        db.session.add(quiz)
        quiz = Quiz(attemptNumber=1, questionNum=20, result=4, author=user2)
        db.session.add(quiz)
        quiz = Quiz(attemptNumber=1, questionNum=20, result=1, author=user3)
        db.session.add(quiz)
        quiz = Quiz(attemptNumber=1, questionNum=20, result=4, author=user4)
        db.session.add(quiz)
        db.session.commit()
        
        expected_passrate = 3/4 * 100
        
        self.assertEqual(QuizController.get_passrate(), expected_passrate)
        
    def test_make_piegraphs(self):
        pass

if __name__=='__main__':
    unittest.main(verbosity=2)