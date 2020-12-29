from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    
    
