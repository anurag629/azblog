from django.shortcuts import redirect, render
from collagepaper.models import Collage, Branch, Paper
from django.http import FileResponse
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


def paper(request):
    if request.method == "POST":
        collage_name = request.POST['collage_name']
        branch_name = request.POST['branch_name']
        year = request.POST['year']
        papers = Paper.objects.filter(
            collage=collage_name, branch=branch_name, paper_year=year)
        data = {
            'papers': papers,
        }
        return render(request, 'collagepaper/paper_list.html', data)
    else:
        return redirect(index)


def paper_pdf(request, paper_code):
    paper = Paper.objects.get(paper_code=paper_code)
    data = {
        'paper': paper,
    }
    return render(request, 'collagepaper/paper_pdf.html', data)
