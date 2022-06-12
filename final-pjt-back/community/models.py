from django.db import models
from django.conf import settings
from movies.models import Movie

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='articles')
    title = models.CharField(max_length=100)
    # movie_title = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='article', null=True)
    # rank = models.IntegerField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)