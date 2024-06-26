"""
URL configuration for news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news_app.views import ArticleCreate, ArticleDelete, ArticleUpdate, PostsList
from django.views.generic import RedirectView

handler404 = 'news_app.views.error_404'
handler403 = 'news_app.views.error_403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news_app.urls')),
    path('articles/', PostsList.as_view(), name='articles'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('articles/<int:pk>/', RedirectView.as_view(url='/news/%(pk)s/')),
    path('', RedirectView.as_view(url='news/')),
    path('accounts/', include('allauth.urls')),
    path('login/', include('sign.urls')),
]
