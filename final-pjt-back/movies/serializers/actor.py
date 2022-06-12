from ..models import Actor, Movie
from rest_framework import serializers
# from .movie import MovieSerializer



class ActorListSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id','title', 'poster_path')
    movie = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        exclude = ('movie_id', 'like_users', 'character')
        read_only_fields = ('movie',)
        depth = 1

class ActorSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id','title',)
    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'