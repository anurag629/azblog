from email.mime import image
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
