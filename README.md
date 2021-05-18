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
 - Add a user to the database: `$python3 populate_database add_user`
 - Add quizzes to database (so the histogram in results page is populated): `$python3 populate_database add_quizzes`
 - Print out questions:`$python3 populate_database print_questions`
 - Print out results: `$python3 populate_database print_results`
 - Print out quiz entries: `$python3 populate_database print_quiz`
 - Print out all answers: `$python3 populate_database print_answers`
 - You can clear the database by:
   - `$python3 populate_database remove_questions`
   - `$python3 populate_database remove_users`
   - `$python3 populate_database remove_answers`
   - `$python3 populate_database remove_quizzes`
```
This will allow you to login to the website using 
Username: newuser
Password: forex1234
Alternatively, you can create an account after launching the app
```
5. `flask run`

This should start the app running on localhost at port 5000, i.e. [http://localhost:5000/index](http://localhost:5000/index)

## Architecture of the Website
When launching the website, it takes you to the home page, explaining the purpose and some general information about the website. You can then choose to go through the topics by clicking the learn tab. To complete the quiz and to view results you must be logged in. So, you can sign up using the link in the top navbar. After signing up you will be redirected to a sign in page. After signing in you can take the quiz. During the quiz, you can leave and it will save your progress. After completing the quiz, you will be redirected to a results page. This page will show you your result for the quiz, the answers for each question and a pie chart showing the number of times each choice has been selected. You can also see a histogram of results under the aggregate results section as well as some additional aggregate information. There is also a leaderboard where you can see the top 3 quiz results and who scored them. You can also go to a view profile section to change your password or email.

## Running the tests
To run the unit tests: `$python3 tests.py`

## Deployment
Via localhost

## Built With
Using git and Visual Studio Code

## Authors
 - Anders Christensen
 - Michael Shawkat


## Git Logs
commit 0f101a983ec9672135ff1b6c5e721834bda1ad55
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Mon May 17 17:51:49 2021 +0800

    Adding flask code

commit 9f6210770d90a036790c9eea00c651e83d0a3248
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Mon May 17 17:34:27 2021 +0800

    Update README.md
    
    Updated database info

commit bd56d5496de85f025ff976ffa97d1aa88bc69323
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Mon May 17 17:21:14 2021 +0800

    Update README.md
    
    Adding in populate database information

commit 68f53977f2d76b867ff8a7b20d2b5f0368daa6ae
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Mon May 17 17:17:04 2021 +0800

    Update README.md
    
    Architecture of website updated

commit 1306abadf245b394ec91a5dfe863d029761fb0d6
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Mon May 17 17:05:00 2021 +0800

    Updated Readme
    
    Added Purpose

commit aa81cee861b9b0e2c331eec7c2f84a80e9610b86
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Mon May 17 16:49:38 2021 +0800

    Updating date

commit a419955cc7360e967bc0f69f6c1fde5f5c7b7a8d
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Mon May 17 16:44:50 2021 +0800

    Updating readme
    
    Adding info on populating the database

commit d4f90396ff25bd9c8472c97119a353c1aa989da9
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Mon May 17 16:35:58 2021 +0800

    Updating Readme
    
    Adding getting started, installing, running tests and deployment

commit 0e728049674fc78e0edd97e4d68846c95204ed5a
Merge: 0b32aac 6ac2a20
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Sun May 16 09:29:27 2021 +0800

    Merge pull request #7 from anders-m-c/anders2
    
    Updating routes, adding some content pages

commit 0b32aac49b6169aa801ab1a26c642c9125312978
Merge: e5eee66 e52f47e
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Sun May 16 09:27:20 2021 +0800

    Merge pull request #6 from anders-m-c/CSMike19-Branch-2
    
    Updating Templates

commit 6ac2a201e5dc64d580c340bc44f892336c332359
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Sun May 16 00:43:48 2021 +0800

    Updating routes, adding some content pages

commit e5eee66c1a8a7d5d3a4b20f13b39d59241d5454e
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Sat May 15 00:28:11 2021 +0800

    Updating routes and quiz pages

commit f4f76a2f57429986ac13050d19a41904b17b98d0
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Sat May 15 00:24:24 2021 +0800

    Removing non flask html pages

commit e52f47e91570b364ed01f831fbff413cd2f601c5
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Fri May 14 19:07:00 2021 +0800

    Updating Templates
    
    Adding Index and Results Page

commit 50b04f4d1beabf6060b63225980ba8208a77afa8
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Tue May 11 23:37:27 2021 +0800

    adding forms

commit 1c86dc59087a9f9e7678c702addac213f20cb460
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Tue May 11 23:27:19 2021 +0800

    updating routes and models

commit b71938937fb784fc94ce1223ce28b7fb01635b30
Merge: d81e8a2 8ae7009
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Sun May 9 22:03:55 2021 +0800

    Merge pull request #5 from anders-m-c/CSMike19-Template
    
    Updated Flask App

commit 8ae70097e2938437e89ecfb2bc3b9504d6d8025f
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Sun May 9 22:02:22 2021 +0800

    Updated Flask App
    
    Quiz, Sign In Page and Login Page added to flask app

commit d81e8a278d1872800b348ec71d4795ce08895d16
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Sun May 9 21:49:37 2021 +0800

    Adding a base.html to flask app

commit b96523e8cad86a8b155bd83dc614133c9f7ead34
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Fri May 7 23:27:30 2021 +0800

    Initial flask app additions

commit 1964646f4247f9a2e78643bc57fe9bc42636ace8
Merge: 9e2fa46 440dc0c
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Tue May 4 22:13:48 2021 +0800

    Merge pull request #4 from CSMike19/main
    
    Made small changes to learn.html and learn2.html

commit 440dc0c35b4a27ae9576cdac19b02d2149aa75f6
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Tue May 4 22:11:55 2021 +0800

    Updated learn2.html

commit 8f7d72588cb89b2f71d78f5a093700845c60b41c
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Tue May 4 22:11:24 2021 +0800

    Update learn.html

commit ead4d56f2f5183968459c15b50c11677bf745263
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Tue May 4 22:07:37 2021 +0800

    Created what is forex page

commit abf04fefd8f8e9e14127a47ca6eef9a10a2dbbb3
Merge: bd1b07e 9e2fa46
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Tue May 4 22:01:36 2021 +0800

    Merge pull request #3 from anders-m-c/main
    
    Updating forked repo

commit 9e2fa469a221ae6a7e84f8a88c45ce78e6c0f1d5
Merge: 4a59c78 bd1b07e
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Tue May 4 21:59:10 2021 +0800

    Merge pull request #3 from CSMike19/main
    
    Merge pull request #2 from anders-m-c/main

commit 4a59c78193c3f8b07d439da728e221688208d2aa
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Tue May 4 21:56:24 2021 +0800

    Added wireframe for homepage

commit dc4a39bd76e1b02206d70582c8825e54b6b64956
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Tue May 4 21:54:17 2021 +0800

    Wireframe for quiz page

commit 2b39471dc024098cd385ce6f4ab99552540aa445
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Sun May 2 22:43:03 2021 +0800

    Adding wireframes for the feedback page

commit 2b631f80f63b54d1b46207b3d8d1996412822ec4
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Sat Apr 24 21:51:22 2021 +0800

    Added sign-up page

commit f08a1a6976f88ff9c35e0eb4a72365a29e4c11f5
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Sat Apr 24 21:50:02 2021 +0800

    Added Login Page
    
    Navbar still needs fixing.

commit bd1b07e5bda951b43064145d88efcc0efac28cef
Merge: c5a3b6e 5064c82
Author: CSMike19 <50289252+CSMike19@users.noreply.github.com>
Date:   Thu Apr 22 12:02:54 2021 +0800

    Merge pull request #2 from anders-m-c/main
    
    Updating Forked Repo

commit 5064c82753823f451c1ffae9c9d089fa1ed3eec8
Merge: 2c8e2a3 c5a3b6e
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Thu Apr 22 12:01:27 2021 +0800

    Merge pull request #2 from CSMike19/main
    
    Merge pull request #1 from anders-m-c/main

commit 2c8e2a3a843df3c40069f2c6c5c4ce2e6a53154e
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Thu Apr 22 11:59:42 2021 +0800

    Adding the intermediate learn home page

commit c5a3b6ef1a8a51e4b352e8b402255682691c619b
Merge: 1c019ee 0518b1d
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Thu Apr 22 11:56:36 2021 +0800

    Merge pull request #1 from anders-m-c/main
    
    Updating CSMike19 fork

commit 0518b1d0e7b0a0513d56f47ddf8586e5444ae4d7
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Thu Apr 22 11:37:41 2021 +0800

    Adding the beginner learn home page

commit caddd42d0df6e69be929e9b67918afabcdc1367c
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Thu Apr 22 11:34:48 2021 +0800

    update gitignore

commit b02aac1389ceb6655369ccc6bf9fb491a5628e8f
Merge: 97c15b4 1c019ee
Author: anders-m-c <51845715+anders-m-c@users.noreply.github.com>
Date:   Thu Apr 22 11:27:49 2021 +0800

    Merge pull request #1 from CSMike19/main
    
    Added Homepage

commit 1c019ee5064ce45095ff60fa2721858fbfd26a61
Author: Michael Shawkat <22716865@student.uwa.edu.au>
Date:   Thu Apr 22 11:15:15 2021 +0800

    Added Homepage

commit 97c15b4d6530580eeb2607023ac414bd0128ae8c
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Thu Apr 22 10:55:20 2021 +0800

    README.md added

commit 780acaa6f74376e99392000815938ddae0bf66bc
Author: anders-m-c <christensen.anders945@gmail.com>
Date:   Thu Apr 22 10:46:43 2021 +0800

    Flask skeleton



