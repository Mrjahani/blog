from django.shortcuts import render , get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse , Http404
from .models import Post
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from blog.models import *
from datetime import datetime

def index(request):
    articles = Article.objects.filter(status='p').order_by('-publish')
    categories = Category.objects.filter(status = True)
    context = {
        'articles' : articles,
        'categories' : categories
    }
    return render(request,'index.html', context)
    #return HttpResponse("hi masoud")
    #all_post = Post.object.all()


@csrf_exempt
def test(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token =this_token).get()
    Expense.objects.create(user=this_user,amount=request.POST['amount'],
        text = request.POST['text'],date=datetime.now())
    return JsonResponse({'status':'ok'},encoder=JSONEncoder)
 

    #return HttpResponse('test bahali bod') 

def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    expenses = Expense.objects.all()
    return render(request,'create.html',{'expenses':expenses})



def post(request, id):
    try:
        # post = get_object_or_404(Post,id=id)
        post = Post.objects.get(id=id)
        context = {
            'post':post
        }
        return render(request , 'posts.html' , context) 

    except:
        raise Http404("No MyModel matches the given query.")

def article(request):
    # record hara filter mikonad va tanha 2 ta record akahr ra namayesh midahad
    articles = Article.objects.filter(status = "p").order_by('-publish')[:2]
    return render(request,'article.html',{'articles':articles})


def detail(request , slug):
    # article = Article.objects.get(slug = slug)
    article = get_object_or_404(Article,slug = slug)
    context = {
        'article' : article
    }
    return render(request , "detail.html" , context)


def category(request , slug):
    category = get_object_or_404(Category , slug=slug)
    categories = Category.objects.filter(status = True)
    context = {
        'category':category,
        'categories' : categories
    }
    return render(request , 'category.html' , context)

