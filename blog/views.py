from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from blog.models import *
from datetime import datetime
from django.shortcuts import get_list_or_404, get_object_or_404

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})
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
    expenses = Expense.objects.all()
    return render(request,'create.html',{'expenses':expenses})



def post(request, id=None):
    post = get_object_or_404(Post,id=id)
    return "ok shod" 
