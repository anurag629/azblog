from email import message
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
    return render(request, 'blog/index.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    count_visitors = Post.objects.get(url=url)
    count_visitors.count_visitor = count_visitors.count_visitor + 1
    count_visitors.save()
    data = {
        'post': post,
        'cats': cats,
    }
    return render(request, 'blog/post.html', data)


def about(request):
    cats = Category.objects.all()
    data = {
        'cats': cats,
    }
    return render(request, 'blog/about.html', data)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        cats = Category.objects.all()
        data = {
            'cats': cats,
            'name': "Thanks! " + name + " We received your contact details and will respond shortly.....",
        }

        return render(request, 'blog/contact.html', data)

    else:
        cats = Category.objects.all()
        data = {
            'cats': cats,
        }
        return render(request, 'blog/contact.html', data)


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    cats = Category.objects.all()
    data = {
        'cats': cats,
        'cat': cat,
        'posts': posts
    }
    return render(request, 'blog/category.html', data)
