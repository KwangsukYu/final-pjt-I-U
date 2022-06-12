from django.db import models
from django.conf import settings
# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.genre_name

class Actor(models.Model):
    movie_id = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    character = models.CharField(max_length=50)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors', blank=True)
    profile_path = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    released_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    poster_path = models.CharField(max_length=300, null=True)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    popularity = models.FloatField()
    recommend_movies = models.ManyToManyField('self', symmetrical=False, related_name = 'recommended', blank=True)


    # like_users
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    actors = models.ManyToManyField(Actor, related_name='actor_movie')
    # video
    video_path = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.title