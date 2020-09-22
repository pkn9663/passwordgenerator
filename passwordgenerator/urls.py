"""
Definition of urls for passwordgenerator.
"""

from datetime import datetime
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from generator import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('generatedpassword/', views.password, name='password'),
    path('about/', views.about, name='about'),  
]
