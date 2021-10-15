from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('index', views.index),
    path('about', views.about),
    path('contact', views.contact, name='contact'),
    path('post/<slug:url>', views.post),
    path('category/<slug:url>', views.category),
]
