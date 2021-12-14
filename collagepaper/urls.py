from django.urls import path, include
from . import views

urlpatterns = [
    path('paper', views.index),
]
