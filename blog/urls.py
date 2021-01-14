from django.urls import path

from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('test/' , views.test , name='test'),
    path('create/' , views.create , name='create'),
    path('<int:id>/' , views.post , name='posts'),
]
