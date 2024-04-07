from django_filters import FilterSet, CharFilter, DateFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Заголовок содержит')
    author = CharFilter(field_name='author__user__username', lookup_expr='icontains', label='Автор содержит')
    pub_date__gt = DateFilter(
        field_name='pub_date',
        label='Дата публикации позже',
        lookup_expr='gt',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'pub_date__gt'
        ]
