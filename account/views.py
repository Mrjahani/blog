from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView
from blog.models import *
from .mixins import FieldMixin , FormValidMixin

@login_required
def home(request):
    context = {
        'articls':Article.objects.all(),
    }
    return render(request,'registration/home.html' , context)

class ArticleList(LoginRequiredMixin , ListView):
    queryset = Article.objects.all()
    template_name = 'registration/all_articles.html'

class ArticleCreate(LoginRequiredMixin , FieldMixin , FormValidMixin , CreateView):
    model = Article
    template_name = 'registration/article_create_update.html'