from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from .models import Movie, Genre, Actor
from .makeDB import makeDB, makeActorDB, makeVideoDB
from django.views.decorators.http import require_safe
from django.core.paginator import Paginator
from .recommendMovie import movie_recommend
from django.db.models import Q

from .serializers.actor import ActorListSerializer, ActorSerializer
from .serializers.movie import MovieSerializer, MovieListSerializer, RecommendMovieSerializer
from .serializers.genre import GenreListSerializer
# from .serializers.review import ReviewSerializer, ReviewListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .like_recommend import recommend_like_movie, find_sim_movie_item
# Create your views here.

@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'movies' : page_obj,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
    
def get_api(request):
    makeDB()
    return redirect('movies:index')

def get_actor(request):
    makeActorDB()
    return redirect('movies:index')

def recommend(request):
    movie_recommend()
    return redirect('movies:index')


# movie 관련 추천
@api_view(['GET'])
def site_ranking_movie_list(request):

    movies = get_list_or_404(Movie.objects.order_by('-popularity')[:10])
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)   

@api_view(['GET'])
def nowplay_ranking_movie_list(request):
    from datetime import date, timedelta
    today = date.today()
    one_month = timedelta(weeks=4)
    movies = get_list_or_404(Movie.objects.order_by('-popularity'))
    movie_data = []
    for movie in movies:
        if today-one_month <= movie.released_date < today:
            movie_data.append(movie)
        if len(movie_data) == 10:
            break
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)


# article 좋아요 순으로 세개
@api_view(['GET'])
def movies_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def movies_recommend(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    rmd_lst = []
    for rmd_movie in movie.recommend_movies.all():
        rmd_lst.append(rmd_movie)
    serializer = MovieListSerializer(rmd_lst, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actors_detail(request, actor_name):
    actor = get_list_or_404(Actor, name=actor_name)
    serializer = ActorListSerializer(actor, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    if user.favorite_movies.filter(pk=movie_pk).exists():
        user.favorite_movies.remove(movie)
        data = 'remove'
    else:
        user.favorite_movies.add(movie)
        data = 'add'
    
    return Response({'data': data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_actor(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    user = request.user
    if user.favorite_actor.filter(pk=actor_pk).exists():
        user.favorite_actor.remove(actor)
        data = 'remove'
    else:
        user.favorite_actor.add(actor)
        data = 'add'
    
    return Response({'data': data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def watch_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    if user.watched_movies.filter(pk=movie_pk).exists():
        user.watched_movies.remove(movie)
        data = 'no watch'
    else:
        user.watched_movies.add(movie)
        data = 'watched'
    
    return Response({'data': data})


@api_view(['POST'])
def search(request):
    keyword = request.data.get('keyword')
    movies = Movie.objects.filter(
        Q(title__contains=keyword)
        # Q(actors__contains=keyword)
    ).distinct()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 장르 리스트
@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre_movie(request, genre_id):
    genre = Genre.objects.get(genre_id=genre_id)
    movies = genre.movie_set.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def like_movie_recommend(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    item_sim_df = recommend_like_movie()
    like_rmd_lst = find_sim_movie_item(item_sim_df, movie.title)
    rmd_id_lst = []
    for rmd_title in like_rmd_lst:
        mv = Movie.objects.get(title=rmd_title)
        rmd_id_lst.append(mv)
    if len(rmd_id_lst) < 5:
        for rmd_movie in movie.recommend_movies.all():
            print(rmd_movie)
            rmd_id_lst.append(rmd_movie)
            if len(rmd_id_lst) == 5:
                break
    serializer = MovieListSerializer(rmd_id_lst, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def random_movie(request):
    import random
    movies = Movie.objects.order_by('-pk')
    for movie in movies:
        last_n = movie.id
        break
    lst = [i for i in range(1, last_n+1)]
    movie_pk_lst = random.sample(lst, 8)
    movie_lst = []
    for movie_pk in movie_pk_lst:
        movie = Movie.objects.get(pk = movie_pk)
        movie_lst.append(movie)
    serializer = MovieListSerializer(movie_lst, many=True)
    return Response(serializer.data)
    