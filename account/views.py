from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView , UpdateView
from django.views.generic.edit import DeleteView
from blog.models import *
from .mixins import FieldMixin , FormValidMixin , AuthorAccessMixin , SuperUserAccessMixin

@login_required
def home(request):
    context = {
        'articls':Article.objects.all(),
    }
    return render(request,'registration/home.html' , context)

class ArticleList(LoginRequiredMixin , ListView):
    template_name = 'registration/all_articles.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)

class ArticleCreate(LoginRequiredMixin , FieldMixin , FormValidMixin , CreateView):
    model = Article
    template_name = 'registration/article_create_update.html'

class ArticleUpdate(AuthorAccessMixin , FieldMixin , FormValidMixin , UpdateView):
    model = Article
    template_name = 'registration/article_create_update.html'

class ArticleDelete( SuperUserAccessMixin , DeleteView):
    model = Article
    success_url = reverse_lazy('account:articles')
    template_name = 'registration/article_confirm_delete.html'