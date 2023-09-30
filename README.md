# Task management
A restful application for managing tasks 

## Description

This is a restfull chat application built with Django and DjangoRestFramework.
used JWT Authentication and celery for background tasks.

## Features

- CRUD operations for tasks
- User registration and authentication
- Email verification
-
- Test cases for user registration and celery
- Enabled development and production mode for project

## Installation

1. Clone the repository
2. Change into the project directory
3. Install the required dependencies
4. Apply database migrations
5. Make sure redis is runnig and listening on port 6379
6. Start the development server
7. Open another terminal and run celery worker using command:
   celery -A task_manager.celery worker --loglevel=info

Note: dont forget to create your .env file
