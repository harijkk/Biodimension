from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.


def home(request):
    # load all posts from database
    posts = Post.objects.all()[:11]
    # print(posts)
    data = {
        'posts': posts
    }
    return render(request, 'home.html', data)


def post(request, post_id):
    post = Post.objects.get(post_id=post_id)
    data = {
        'post': post
    }
    print(post)
    return render(request, 'post.html', data)
