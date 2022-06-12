from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Actor
from community.models import Article

class User(AbstractUser):
    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    favorite_actors = models.ManyToManyField(Actor, blank=True, related_name='actor_users')
    favorite_movies = models.ManyToManyField(Movie, blank=True, related_name='movie_users')
    watched_movies = models.ManyToManyField(Movie, blank=True, related_name='movie_watched')
    favorite_article = models.ManyToManyField(Article, blank=True, related_name='article_users')