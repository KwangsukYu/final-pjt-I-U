from django.contrib import admin
from .models import Movie, Genre, Actor
# Register your models here.

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
