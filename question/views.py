from django.shortcuts import render

def index(request):
    return render(request, 'question/index.html', {})

def new_question(request):
    return render(request, 'question/new_question.html', {})