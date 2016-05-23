from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from models import Question


def test():
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 2))
    except ValueError:
        limit = 10
    if limit < 1 or limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def index(request):
    questions = paginate(request, Question.objects.order_by('-added_at'))
    return render(request, 'index.html', {
        'questions': questions
    })


def popular(request):
    questions = paginate(request, Question.objects.order_by('-rating'))
    return render(request, 'index.html', {
        'questions': questions
    })


def question(request, id):
    try:
        q = Question.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'question.html', {
        'question': q,
        'answers': q.answer_set.all
    })
