from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating(self):
        author_post = Post.objects.filter(author = self)
        author_comment = Comment.objects.filter(user = self.user)
        others_comment = Comment.objects.filter(post__author = self)
        author_post_rate, author_comment_rate, others_comment_rate = 0, 0, 0
        for e in author_post:
            author_post_rate += e.rating
        for e in author_comment:
            author_comment_rate += e.rating
        for e in others_comment:
            others_comment_rate += e.rating
        self.rating = author_post_rate * 3 + author_comment_rate + others_comment_rate
        self.save()
        
class Category(models.Model):
    name = models.CharField(max_length = 255, unique = True)

class Post(models.Model):
    news = 'NE'
    article = 'AR'
    variant = [
        (news, 'Новость'), 
        (article, 'Статья')]
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    _type = models.CharField(max_length = 2, choices = variant, default = news)
    pub_date = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 255)
    text = models.TextField()
    rating = models.IntegerField(default = 0)
    category = models.ManyToManyField(Category, through = 'PostCategory')

    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:21] + '...'
    
    def __str__(self):
        return f'{self.title}: {self.preview()}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()
    