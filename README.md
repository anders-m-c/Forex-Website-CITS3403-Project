# CITS3403 Project - Forex Website
#### Written in 2021
## Purpose 
The purpose of this website is to educate users on the Forex market and how to trade effectively. The website covers a variety of topics from the fundamentals of forex trading, up to the more advanced topics. This website provides an interactive quiz where users can test their knowledge on the materials covered. Additionally, a results page is included that displays quiz aggregate results, usage statistics and a leaderboard based on quiz results.
## Getting Started
Create a python virtual environment by: `$python3 -m venv venvname`

Activate the python virtual environment: `$source venvname/bin/activate`

To run the app: `$flask run`

To stop the app `$^C`

### Prerequisites
Requires python3, flask, venv, sqlite, pandas

### Installing
Install python3, sqlite

1. Set up a virtual environment:
 - use pip or another package manager to install virtualenv package `$pip3 install virtualenv`
 - start the provided virtual environment
   `$source virtual-environment/bin/activate`
 - To install all the required packages: `$pip3 install -r requirements.txt`
2. Install sqlite
 - [Windows instructions](http://www.sqlitetutorial.net/download-install-sqlite/)
 - In \*nix, `$sudo apt-get install sqlite`
3. Build the database: `$flask db init`
4. Populate the database by completing the folllowing:
 - Add questions to database: `$python3 populate_database add_questions`
 - Add a user to the database: `python3 populate_database add_user`
```
This will allow you to login to the website using 
Username: newuser
Password: forex
Alternatively, you can create an account after launching the app
```
5. `flask run`

This should start the app running on localhost at port 5000, i.e. [http://localhost:5000/index](http://localhost:5000/index)

## Running the tests
To run the unit tests: `$python3 tests.py`

## Deployment
Via localhost

## Built With
Using git and Visual Studio Code

## Authors
 - Anders Christensen
 - Michael Shawkat

## Acknowledgements
 - Built following the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg.






