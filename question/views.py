from django.shortcuts import render

def index(request):
    return render(request, 'question/index.html', {})

def ask(request):
    return render(request, 'question/ask.html', {})

def question(request):
    return render(request, 'question/question.html', {})

