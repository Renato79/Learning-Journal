"""Defines URL patterns for learning_journals."""

from django.urls import path
from . import views


app_name = 'learning_journals'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
