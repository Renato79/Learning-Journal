from django.shortcuts import render



def index(request):
    """Home Page for learning_journals"""
    return render(request, 'learning_journals/index.html')