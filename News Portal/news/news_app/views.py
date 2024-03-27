from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


class PostsList(ListView):
    model =  Post
    ordering = 'name'
    template_name = 'posts.html'
    context_object_name = 'post'
