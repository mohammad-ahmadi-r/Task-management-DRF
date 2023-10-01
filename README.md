## Task Management App
## Overview

- This is a Restful task management application that allows users to create, read, update, and delete (CRUD) tasks. 
- It also includes features such as email verification and the ability to mark tasks as "liked".
- The application uses Celery for background processing and JSON Web Tokens (JWT) for authentication.

## Environment Modes
The application has two environment modes:

- Dev: This is the development environment, which is used for testing and debugging purposes.
- Prod: This is the production environment, which is used for the live application.
  
## Setting Up The Environment
To set up the environment, follow these steps:

- Clone the repository and install dependencies using pip: pip install -r requirements.txt
- Create a .env file and put your variables in it
- Run migrations to set up the database: ./manage.py migrate
- Start the development server: ./manage.py runserver (for dev environment) or ./manage.py runserver 0.0.0.0:8000 (for prod environment)
- Open the application in your web browser at <http://localhost:8000/> (for dev environment) or <https://your-domain.com> (for prod environment)

## Features
# Task CRUD Operations
Users can create, read, update, and delete tasks using RESTful endpoints.

- Create a new task: POST /tasks/
- Retrieve all tasks: GET /tasks/
- Retrieve a single task by ID: GET /tasks/{id}
- Update a task: PUT /tasks/{id}
- Delete a task: DELETE /tasks/{id}
- Email Verification
- The application uses email verification to ensure that user accounts are authenticated. 
- Then you will receive an email with a link to verify their account. Until the user clicks on this link, their account will be marked as unverified.
- POST /users/request-verification/  with username or email in body

# Like Option
Users can mark tasks as "liked" by clicking on the heart icon next to each task. This feature uses a separate endpoint to handle likes.

- Like and Dislike a task: PATCH /tasks/like/ with task_id in body

# Background Processing
The application uses Celery to handle background processing of tasks. For email sending to user, it'll be added to a queue and processed asynchronously.
- In another terminal run this command -> celery -A task_manager.celery worker --loglevel=info

# Authentication
The application uses JSON Web Tokens (JWT) to manage user sessions. Users must provide a valid username and password to retrieve access and refresh token.
Use bearer token to have access to your tasks and ...

# Testing
The application includes test cases for user registration, email sending. To run the tests, use the following command: 
   - python manage.py test users.tests.EmailRegistrationTest
   - python manage.py test users.tests.UserRegistrationTest 


# API Endpoints
Here are some examples of API endpoints available in the application:

- /tasks: Retrieves a list of all tasks
- /tasks/{id}: Retrieves a specific task by ID
- /tasks/like  "task_id":n -> Likes and Unlikes a task

# Technical Details
- The application is built using Django Rest Framework (DRF) and Python 3.10.
- The application uses Sqlite as its database.


# Contributing
Pull requests are welcome! Please open a pull request with a description of the changes you would like to make.

# Issues
If you encounter any issues, please open a ticket on GitHub and include detailed steps to reproduce the issue.
