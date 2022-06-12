from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Article
from .comment import CommentSerializer
from movies.models import Movie, Actor
# from movies.serializers.movie import MovieSerializer
User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)
            depth = 1
        
    class MovieSerializer(serializers.ModelSerializer):
        class ActorSerializer(serializers.ModelSerializer):
            class Meta:
                model = Actor
                fields = ('id','name','profile_path')
        actors = ActorSerializer(many=True, read_only=True)
         
        class Meta:
            model = Movie
            fields = ('id','title','poster_path','actors')
            depth = 1
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    # choice = serializers.ChoiceField(choices=user.like_movies)
    article_users = UserSerializer(read_only=True, many=True) # 좋아요
    like_count = serializers.IntegerField(source="article_users.count",read_only=True)
    movie = MovieSerializer(read_only = True)
    class Meta:
        model = Article
        # fields = ('pk', 'user', 'title','movie', 'content', 'comments', 'like_users')
        fields = '__all__'


# Article List Read
class ArticleListSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title','poster_path')
            depth = 1
    movie = MovieSerializer(read_only=True)
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)

    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source="comments.count", read_only=True)
    article_users = UserSerializer(read_only=True, many=True) # 좋아요
    like_count = serializers.IntegerField(source="article_users.count",read_only=True)
    
    class Meta:
        model = Article
        fields = ('pk', 'user','movie', 'title', 'comments','comment_count', 'article_users','like_count','content')

