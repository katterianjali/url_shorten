README

# URL Shorten 

This project aims to shorten a given url using python,gunicorn and SQLite. 



Use IDEs like pycharm to clone and import this project using the code repository OR install python and gunicorn in your CLI and import this project conents. 
 https://github.com/katterianjali/url_shorten.git


## The scope involves 

+ Shorten a given URL into smaller length random string.
+ This random generated string can then be used to redirect to the actual URL.
+ When the requested URL for shorten was processed earlier, this code checks the existing DB before creating a new one.
+ Once the URL is matched in the DB data, the shortened URL in the DB is returned.
+ This provide the code functionality to give a unique id for each given URL.

## Prerequisits

+ A local Python 3 programming environment.
+ IDE - Pycharm latest version.
+ Gunicorn framework for building the application.
+ API testing tool - POSTMAN.

## Running application from Terminal

+ Install Python latst version. 
+ Follow the below mentioned steps to create a virtual environment and install flask and gunicorn in it before running the application. 
  + mkdir api_test
  + cd api_test
  + python3 -m venv fl_venv
  + ls -ltr
  + . fl_venv/bin/activate
  + pip install Flask 
  + pip list
  + pip install hashids
  + pip install gunicorn
+ Copy the contents of this repo (4 files) in to the same directory of fl_venv. 
+ Execute 'python init_db.py' to initialize the DB.
+ Execute the application using below command.
  + gunicorn -b 0.0.0.0:5001 app:app
+ Test the application in any API tester.
+ Execute 'python utils.py' to check the created DB contents. 


## Running the Application from Pycharm

+ Open Pycharm.
+ New Project - > Get from VCS.
+ Import by cloning remote project from the repository https://github.com/katterianjali/url_shorten.git.
+ Once the project is created in the Pycharm ,
  + set the run configuration for python gunicorn.
    + script path = "your venv"/bin/gunicorn
    + parameters = -b 0.0.0.0:5001 app:app
    + select python intrepreter and working directory.
    + Apply and OK.
  + Execute init_db.py in current file execution mode to create the database table.
  + Execute app.py to run the application usng gunicorn mode.
  + Test the application in any API Tester.
  + Execute utils.py in current file execurion mode to check the contents inside table after execution.
  

## Testing the Application

+ Open Postman
+ New -> HTTP Request.
+ Input the application URL (http://127.0.0.1:5001/shorten) -> Select the request method.
+ Enter the request payload in the json format (raw).
+ Send the request.
+ The response received will be the shortened URL.
+ Input the response in any browser which will be redirected to the actual URL. 
