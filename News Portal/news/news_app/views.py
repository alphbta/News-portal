from typing import Any
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostsList(ListView):
    model =  Post
    ordering = '-pub_date'
    template_name = 'news.html'
    context_object_name = 'news'

class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    