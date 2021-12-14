from django.shortcuts import render
from collagepaper.models import Collage, Branch, Paper
# Create your views here.


def index(request):
    collage = Collage.objects.all()
    branch = Branch.objects.all()
    paper = Paper.objects.all()
    data = {
        'collages': collage,
        'branchs': branch,
        'papers': paper,
    }
    return render(request, 'collagepaper/paper.html', data)
