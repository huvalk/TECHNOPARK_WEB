from django.shortcuts import render
from question.models import Queion
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist



def index(request):
    res = Queion.objects.all()
    return render(request, 'question/index.html', {'tag': "Question",
                                                   'res': res})


def hot(request):
    return render(request, 'question/index.html', {'tag': "Hot"})


def tag(request, val="Questions"):

    return render(request, 'question/index.html', {'tag': val})


def ask(request):
    return render(request, 'question/ask.html', {})


def question(request, val):
    #TODO get кидает исключения
    try:
        res = Queion.objects.get(pk=val)
        return render(request, 'question/question.html', {'res': res})
    except ObjectDoesNotExist:
        raise Http404


def login(request):
    return render(request, 'question/login.html', {})


def register(request):
    return render(request, 'question/register.html', {})