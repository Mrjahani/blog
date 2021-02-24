from django.urls import path

from . import views
# from .views import ArticleList

urlpatterns = [
    # class base view
    # path('' , ArticleList.as_view() , name='index'),
    path('' , views.index , name='index'),
    path('test/' , views.test , name='test'),
    path('create/' , views.create , name='create'),
    path('posts/<int:id>/' , views.post , name='posts'),
    path('articles/' , views.article , name="articles"),
    path('articles/<slug:slug>', views.detail , name="detail_artilce"),
    path('categories/<slug:slug>' , views.category , name="category"),
]
