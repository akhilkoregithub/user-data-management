# Task Description:
Create a simple listing for the User Data Managment. 

Use Django Web Framework for the project. 

Create the project in a virtual environment. Make requirements.txt file with all libraries used for the project. Use default Sqlite as a database.

# User Model (name, email, age, dateofbirth) with validated forms(All fields are mandatory to fill) Add, Update, Delete the employee details.
- User model it's fields
  

# add_user, display_user, update_user and delete_user views.
- if click the sumbit button then user input data stored in sqlite database.
- if click on the reset button to refresh the form page.
- if click on the user_list on navbar to open the users data table page.
- if click the update and delete buttons then update and delete the users data.
- show message notification after each successful function.

# Templates for UI Component for user data form and display data
- user input data form
- user data display table
- user data update form

# Required urls add user data and retrieve user data
- user input data form url endpoint: http://127.0.0.1:8000/add_user/
- user data display url end point: http://127.0.0.1:8000/display-users/
- user data update url end point: http://127.0.0.1:8000/update/

# A few Steps for run the project:
- clone repo from given GitHub url: https://github.com/akhilkoregithub/user-data-management.git
- create virtual environment and activate it
- install dependencies from "requirements.txt" using pip install - r requirements.txt command
- run command "python manage.py migrate"
- run command "python manage.py createsuperuser"
- then run "python manage.py runserver"

# Technologies used:
- Frontend (HTML5 & Bootstrap - 5)
- Backend (Django web framework - 4.0.4)
- Database (SQLite database)

# Note: 
- Internet is required for run the project because of I used bootstrap CDN
