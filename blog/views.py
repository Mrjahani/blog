from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def index(request):
    return HttpResponse("hi masoud")
    #all_post = Post.object.all()

def test(request):
    return HttpResponse('test bahali bod') 
