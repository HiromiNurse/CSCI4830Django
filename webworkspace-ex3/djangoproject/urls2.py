"""
Project-Level URL Configuration (djangoproject)

This file defines the root URL routing for the entire Django project.

Instead of mapping URLs directly to view functions here,
we delegate (forward) all incoming requests to the
hello_world_app URL configuration.

Route Definition:

- ''  → include('hello_world_app.urls')

Meaning:
When a user visits the root URL (e.g., http://<public-ip>:8000/),
Django will load and use the URL patterns defined inside:

    hello_world_app/urls.py

Why use include()?

- Keeps the project modular and organized.
- Separates project-level routing from app-level routing.
- Allows each Django app to manage its own URLs.

Workflow:

User Request → Project urls.py → App urls.py → View → Model → Template → Response
"""
# from django.contrib import admin
from django.urls import path, include
# from hello_world_app.views import hello

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', hello)
    path('', include('hello_world_app.urls')),
]
