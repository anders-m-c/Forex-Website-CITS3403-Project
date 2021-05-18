import unittest, os, time
from app import app, db
from app.models import User, Quiz, Question, Answer
from selenium import webdriver
basedir = os.path.abspath(os.path.dirname(__file__))
import populate_database


class SystemTest(unittest.TestCase):
    driver = None
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.join(basedir,'chromedriver'))

        if not self.driver:
            self.skipTest('Web browser not available')
        else:
            db.init_app(app)
            db.create_all()
            
            user1 = User(firstname="User1", lastname="user1", username="user1", num_attempts=0, sessionEnded=1)
            user2 = User(firstname="User2", lastname="user2", username="user2", num_attempts=0, sessionEnded=1)
            
            db.session.add(user1)
            db.session.add(user2)
            
            user1.set_password("user123pass")
            db.session.commit()
            self.driver.maximize_window()
            self.driver.get('http://localhost:5000/')

    def tearDown(self):
        if self.driver:
            self.driver.close()
            db.session.query(User).delete()
            db.session.query(Quiz).delete()
            db.session.query(Question).delete()
            db.session.query(Answer).delete()
            db.session.commit()
            db.session.remove()
            
    #Test that a user can signup, creating an account
    def test_signup(self):
        user = User.query.get(1)
        self.assertEqual(user.username,'user1',msg='user exists in db')
        self.driver.get('http://localhost:5000/signup')
        self.driver.implicitly_wait(5)
        
        firstname = self.driver.find_element_by_id('firstname')
        firstname.send_keys('newuser')
        lastname = self.driver.find_element_by_id('lastname')
        lastname.send_keys('newuserlastname')
        username = self.driver.find_element_by_id('username')
        username.send_keys('newuser')
        email = self.driver.find_element_by_id('email')
        email.send_keys('newuser@newuser.com')
        password = self.driver.find_element_by_id('password')
        password.send_keys('newuser1234')
        password2 = self.driver.find_element_by_id('password2')
        password2.send_keys('newuser1234')
        time.sleep(1)
        self.driver.implicitly_wait(5)
        submit = self.driver.find_element_by_id('submit')
        submit.click()
        #check login success
        self.driver.implicitly_wait(5)
        time.sleep(1)
        modal = self.driver.find_element_by_class_name('messages')
        self.assertEqual(modal.get_attribute('innerHTML'), 'Congratulations newuser, you are now a registered user!')
    
    #Test that a user can sign in, given they are a user in the database
    def test_signin(self):
        user = User.query.get(1)
        self.assertEqual(user.username,'user1',msg='user exists in db')
        self.driver.get('http://localhost:5000/signin')
        self.driver.implicitly_wait(10)
        
        username = self.driver.find_element_by_id('username')
        username.send_keys('user1')
        password = self.driver.find_element_by_id('password')
        password.send_keys('user123pass')
        time.sleep(1)
        self.driver.implicitly_wait(5)
        submit = self.driver.find_element_by_id('submit')
        submit.click()
        self.driver.implicitly_wait(5)
        time.sleep(1)
        logout = self.driver.find_element_by_id('logout')
        self.assertEqual(logout.get_attribute('innerHTML'), 'Logout', msg='Logged in')

    #Test if a non-authenticated user is rejected from viewing the results
    #(They should be rejected)
    def test_result_no_auth(self):
        self.driver.get('http://localhost:5000/results')
        self.driver.implicitly_wait(10)
        self.driver.implicitly_wait(5)
        time.sleep(1)
        modal = self.driver.find_element_by_id('main_message')
        self.assertEqual(modal.get_attribute('innerHTML'), '404 Error: Page Not Found')
       
    #Test if a non-authenticated user is rejected from viewing the quiz
    #(They should be rejected) 
    def test_quiz_no_auth(self):
        self.driver.get('http://localhost:5000/quiz/1')
        self.driver.implicitly_wait(10)
        
        modal = self.driver.find_element_by_class_name('messages')
        self.assertEqual(modal.get_attribute('innerHTML'), 'You must log in to view the quiz.')
    
    #Test if a flash message pops up if the try access the results if
    #there are no questions in the database.
    def test_results_no_questions(self):
        self.test_signin()
        self.driver.implicitly_wait(5)
        time.sleep(1)
        self.driver.get('http://localhost:5000/results')
        self.driver.implicitly_wait(5)
        time.sleep(1)
        modal = self.driver.find_element_by_id('main_message')
        self.assertEqual(modal.get_attribute('innerHTML'), '404 Error: Page Not Found')
       
    #Test if a flash message pops up if the try access the quiz if
    #there are no questions in the database. 
    def test_quiz_no_questions(self):
        self.test_signin()
        self.driver.get('http://localhost:5000/quiz/1')
        modal = self.driver.find_element_by_class_name('messages')
        self.assertEqual(modal.get_attribute('innerHTML'), 'Questions have not been added yet. Refer to github.')
        
    #Test if a user doing the quiz will be able to complete the quiz
    #successfully and upon completion be redirected to the results page.
    def test_quiz(self):
        populate_database.add_questions()
        self.test_signin()
        self.driver.get('http://localhost:5000/quiz/1')
        
        self.driver.implicitly_wait(5)
        time.sleep(1)
        
        for i in range(19):
            option = self.driver.find_element_by_id('opt1')
            option.click()
            next_btn = self.driver.find_element_by_id('next_btn')
            next_btn.click()
            self.driver.implicitly_wait(5)
            time.sleep(1)
        
        option = self.driver.find_element_by_id('opt1')
        option.click()
        finish_btn = self.driver.find_element_by_id('finish_btn')
        finish_btn.click()
        
        self.driver.implicitly_wait(5)
        time.sleep(2)
        
        result_msg = self.driver.find_element_by_id('results_title')
        self.assertEqual(result_msg.get_attribute("innerHTML"), "Results for quiz attempt 1")        
        
        
if __name__=='__main__':
  unittest.main(verbosity=2)