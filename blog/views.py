from django.shortcuts import render, redirect
from blog.models import Category, Post
# Create your views here.


def home(request):
    return redirect(index)


def index(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    data = {
        'posts': posts,
        'cats': cats,
    }
    return render(request, 'index.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    data = {
        'post': post,
        'cats': cats,
    }
    return render(request, 'post.html', data)


def about(request):
    cats = Category.objects.all()
    data = {
        'cats': cats,
    }
    return render(request, 'about.html', data)


def contact(request):
    cats = Category.objects.all()
    data = {
        'cats': cats,
    }
    return render(request, 'contact.html', data)


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    cats = Category.objects.all()
    data = {
        'cats': cats,
        'cat': cat,
        'posts': posts
    }
    return render(request, 'category.html', data)
