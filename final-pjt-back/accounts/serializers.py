from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article
from movies.models import Movie, Actor
# from movies.serializers.movie import MovieSerializer
# from movies.serializers.actor import ActorSerializer
class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('id', 'title', 'content')

    favorite_article = ArticleSerializer(many=True, read_only=True)
    favorite_article_count = serializers.IntegerField(source='favorite_article.count', read_only=True)

    articles = ArticleSerializer(many=True, read_only=True)

    # 영화 좋아요
    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'overview')
    
    watched_movies = MovieSerializer(many=True)
    watched_movies_count = serializers.IntegerField(source='watched_movies.count', read_only=True)
    favorite_movies = MovieSerializer(many=True, read_only=True)
    favorite_movies_count = serializers.IntegerField(source='favorite_movies.count', read_only=True)
    # 배우 좋아요
    class ActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('id', 'name', 'profile_path')
    favorite_actors  = ActorSerializer(many=True, read_only=True)
    favorite_actors_count = serializers.IntegerField(source='favorite_actors.count', read_only=True)
    
    class Meta:
        model = get_user_model()
        # fields = ('id', 'username', 'favortie_articles', 'favorite_article_count','articles','favortie_movies','favorite_movies_count','favortie_actors','favorite_actors_count','watched_movies','watched_movies_count')
        fields = '__all__'
