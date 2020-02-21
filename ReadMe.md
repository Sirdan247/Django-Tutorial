Django Blog Tutorial
This project is about how to create a Blog using Django

Resource
https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc

Django docs - https://docs.djangoproject.com/en/1.11/

Installation And Creating New Project
# Install django from terminal
$ pip install django
# Creating a new project called djangonautic
$ django-admin startproject djangonautic
# Create/run a local server for our project
$ python manage.py runserver

URLs And Views
Urls to visit a particular page or view 
Views create output to the browser

HTML Templates
Create templates folder in root directory
create needed template (html) files in the template directory
set dir in settings to ['templates']
import render
change return requests in views to html files using render

Django Apps
Split up project into separate little apps for different sections of our project

# To create an app say articles in the root directory/folder 
$ python manage.py startapp articles 

Register new apps inside project in settings.py under INSTALLED_APPS
Create url files in each app created
Create templates folder in each app
Create a folder with the same name as app inside the template directory
Create needed template files (say html files).

Register apps urls in main urls file inside the project/root app

Import include function
# To register articles directory 
path(‘articles/’, include(articles.urls)),

Django Models

Migrations
Migrate models to a database
A migration file tracks any changes to a model
Perform the two operations below whenever a new file is created or a change is made.
#To Create a migration file 
$ python manage.py makemigrations

# To migrate models 
$ python manage.py migrate
