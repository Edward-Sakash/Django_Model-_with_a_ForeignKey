## Django Exercise: Creating and Displaying a Model with a ForeignKey
### Objective:
To create a Django app that:
1. Has a model with a ForeignKey pointing to Django's built-in User model.
2. Allows users to add entities to this model via the Django admin interface.
3. Displays these entities using a ListView.
4. Provides a detailed view for each entity using a DetailView.
5. Adds static CSS to style both the list and detail views.
### Task:
1. *Set up the Django Project and App*:
    - Create a new Django project called userproject.
    - Create a new app called userapp.
2. *Design the Model with a ForeignKey*:
    - In userapp/models.py, design a model called Profile with a CharField named bio and a ForeignKey to the User model.
3. *Setup Django Admin*:
    - Register the Profile model with the Django admin in userapp/admin.py.
    - Create a superuser and then use the admin interface to add profiles for users.
4. *Display the Model Data*:
    - Use a ListView to display the profiles.
    - Use a DetailView to provide detailed information on each profile.
    - Add static CSS to style both views.
---
### Detailed Instructions:
1. *Set up the Django Project and App*:
bash
    django-admin startproject userproject
    cd userproject
    python manage.py startapp userapp
    
2. *Design the Model with a ForeignKey*:
    userapp/models.py:
python
    from django.db import models

    class Profile(models.Model):
        user = 
        bio = 
        
        def __str__(self):
            return self.user.username
    
3. *Setup Django Admin*:
    userapp/admin.py:
python
    from django.contrib import admin
    from .models import Profile

    ....
    
    - Now, add userapp to INSTALLED_APPS in userproject/settings.py:
python
    INSTALLED_APPS = [
        ...
        'userapp',
    ]
    
    - Run migrations:
bash
    python manage.py makemigrations
    python manage.py migrate
    
    - Create a superuser:
bash
    python manage.py createsuperuser
    
    - Run the server, go to http://localhost:8000/admin/, and use the admin interface to create new user profiles.
4. *Display the Model Data*:
    userapp/views.py:
python
    from django.views.generic import ListView, DetailView
    from .models import Profile

    class ProfileListView(ListView):
        
    class ProfileDetailView(DetailView):
    
    - Create a templates directory inside userapp and then create files named profile_list.html and profile_detail.html.
    userapp/templates/profile_list.html:
html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Profile List</title>
        <link rel="stylesheet" type="text/css" href="{% static 'styles.css' %}">
    </head>
    <body>
        <ul>
            .........
        </ul>
    </body>
    </html>
    
    userapp/templates/profile_detail.html:
html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Profile Detail</title>
        <link rel="stylesheet" type="text/css" href="{% static 'styles.css' %}">
    </head>
    <body>
        <h1>{{ object.user.username }}</h1>
        <p>{{ object.bio }}</p>
        <a href="?????">Back to list</a>
    </body>
    </html>
    
    - Now, setup static files. Create a static directory inside userapp. Inside this directory, create a CSS file named styles.css.
    userapp/static/styles.css:
css
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        padding: 20px;
    }
    ul {
        list-style-type: none;
    }
    li {
        background-color: #e0e0e0;
        padding: 10px;
        margin: 5px 0;
    }
    a {
        color: #333;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    h1 {
        color: #666;
    }
    
    - Update the project's urls.py:
    userproject/urls.py:
python
    from django.urls import path
    from userapp.views import ProfileListView, ProfileDetailView

    urlpatterns = [
        path(????? name='profile-list'),
        path(????? name='profile-detail'),
        ...
    ]
    
5. *Run and Test*:
    - Start the Django server:
bash
    python manage.py runserver
    
    - Visit http://localhost:8000/profiles/ to see the list of profiles. Click on a profile to see its details.