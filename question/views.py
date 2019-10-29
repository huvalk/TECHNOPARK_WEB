from django.shortcuts import render


def index(request):
    return render(request, 'question/index.html', {'tag': "Question"})


def hot(request):
    return render(request, 'question/index.html', {'tag': "Hot"})


def tag(request, val="Questions"):

    return render(request, 'question/index.html', {'tag': val})


def ask(request):
    return render(request, 'question/ask.html', {})


def question(request):
    return render(request, 'question/question.html', {})

