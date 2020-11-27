from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from news.models import Article
from projects.models import Project
#def index(request):
#    return HttpResponse('<h4>Привет TechSpace<br>It`s Work!</h4>')


def index(request):
    articles = Article.objects.order_by('-id')[:3]  # сортировка в обратном порядке 3 последние новсости
    projects = Project.objects.order_by('-id')[:2]
    return render(request, 'home/index.html',
                  {'title': 'Главная страница TechSpace',
                   'articles': articles,
                   'projects': projects})
