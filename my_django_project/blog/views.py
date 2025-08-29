from django.shortcuts import render
from .models import Post

post = [
    {
        'author':"Hanson Han",
        "title": "Blog post 1",
        "content":"Hello",
        "date_posted":"August 27, 2018"
    },
    {
        'author':"Liam Xu",
        "title": "Blog post 2",
        "content":"Hi",
        "date_posted":"August 30, 2018"
    }
]

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':"About"})