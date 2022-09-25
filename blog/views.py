from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Post

all_posts = Post.objects.all().order_by('-date')


def index(request):
    lastest_posts = Post.objects.all().order_by('date')[:3]
    return render(request,"blog/index.html",{'posts': lastest_posts})

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request,slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html",{
        'post': identified_post,
        'post_tags': identified_post.tags.all()
    })
