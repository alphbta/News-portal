from django.urls import path
from .views import PostsList, PostsDetail, NewsCreate, NewsUpdate, NewsDelete


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>/', PostsDetail.as_view(), name='post_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]
