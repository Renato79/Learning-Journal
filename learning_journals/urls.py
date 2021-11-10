"""Defines URL patterns for learning_journals."""

from django.urls import path
from . import views


app_name = 'learning_journal'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
]






