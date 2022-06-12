from ..models import Actor, Movie, Genre
from rest_framework import serializers
# from .movie import MovieSerializer


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'