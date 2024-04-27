from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PostsList(ListView):
    model =  Post
    ordering = '-pub_date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news_app.add_post')
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post._type = Post.news
        return super().form_valid(form)

class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news_app.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news_app.delete_post')
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news_app.add_post')
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post._type = Post.article
        return super().form_valid(form)

class ArticleUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news_app.change_post')
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news_app.delete_post')
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')

def error_404(request, exception):
    return render(request, '404.html', {}, status=404)

def error_403(request, exception):
    return render(request, '403.html', {}, status=403)