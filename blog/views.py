from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views import View

# Create your views here.
from .models import Post
from .forms import CommentForm

class Index(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ["-date"]
    context_object_name = 'posts'

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data

class Posts(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ["-date"]
    context_object_name = 'all_posts'

class SinglePostView(View):

    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id').order_by('-id')[:4]
        }

        return render(request,"blog/post-detail.html", context)


    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if comment_form.is_valid():
            print("It says it is valid")
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse('post-detail-page', args=[slug])) 
        
        print("It says it is not valid")
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id')[:4]
        }

        return render(request,"blog/post-detail.html", context)
    