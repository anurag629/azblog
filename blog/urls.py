from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('post/<slug:url>', views.post),


]
