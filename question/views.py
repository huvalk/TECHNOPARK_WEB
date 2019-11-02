from django.shortcuts import render
from question.models import Question, Answer, Tag, Paginate_by
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    p = request.GET.get('p')
    page = Paginate_by(page=p, order='date')
    return render(request, 'question/index.html', {'headline': "Question",
                                                   'page': page,
                                                   'paginate': 'index'})


def hot(request):
    p = request.GET.get('p')
    page = Paginate_by(page=p, order='rating')
    return render(request, 'question/index.html', {'headline': "Hot",
                                                   'page': page,
                                                   'paginate': 'hot'})


def tag(request, t="Tag"):
    p = request.GET.get('p')
    page = Paginate_by(page=p, order='date', tag=t)
    return render(request, 'question/index.html', {'headline': t,
                                                   'page': page,
                                                   'paginate': 'tag'})


def ask(request):
    return render(request, 'question/ask.html', {})


def question(request, q):
    try:
        ques = Question.objects.get(pk=q)
    except ObjectDoesNotExist:
        raise Http404
    ans = Answer.objects.filter(que=ques.id)
    return render(request, 'question/question.html', {'ques': ques,
                                                      'ans': ans})


def login(request):
    return render(request, 'question/login.html', {})


def register(request):
    return render(request, 'question/register.html', {})