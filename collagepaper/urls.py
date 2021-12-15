from django.urls import path, include
from . import views

urlpatterns = [
    path('collage_paper', views.index),
    path('paper', views.paper, name='paper'),
    path('paper_pdf/<slug:paper_code>', views.paper_pdf),
]
