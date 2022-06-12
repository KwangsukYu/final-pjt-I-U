from ..models import Actor, Movie, Genre
# from .actor import ActorSerializer, ActorListSerializer
from rest_framework import serializers
from ..tmdb import TMDB_API_KEY
from community.serializers.article import ArticleSerializer


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'poster_path', 'vote_average')

class RecommendMovieSerializer(serializers.ModelSerializer):
    recommend_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('recommend_movies',)

class MovieSerializer(serializers.ModelSerializer):
    class ActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('id','name', 'profile_path')
            depth = 1
    actors = ActorSerializer(many=True, read_only=True)
    
    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('genre_name',)
            depth = 1
    genres = GenreSerializer(many=True, read_only=True)

    recommend_movies = MovieListSerializer(many=True, read_only = True)
    
    article = ArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ('recommend_movies',)