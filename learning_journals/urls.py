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
    # Page to add a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page to edit a topic
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    # Page to delete a topic
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    # Page to add a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page to edit an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page to delete an entry
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    # Page with the form contact us
    path('contact_us/', views.contact_us, name='contact_us'),
    # Page with the confirmation that the email has been sent
    path('sent/', views.sent, name='sent'),
]