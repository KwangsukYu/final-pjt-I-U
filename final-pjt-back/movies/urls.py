from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:movie_pk>/', views.detail, name='detail'),
#     path('get_api/', views.get_api, name='get_api'),
#     path('get_actor/',views.get_actor, name='get_actor'),
#     path('recommend/', views.recommend, name='recommend'),
    path('site_rank_movie/', views.site_ranking_movie_list),
    path('nowplay_rank/', views.nowplay_ranking_movie_list),
    path('<int:movie_pk>/', views.movies_detail),
    path('<int:movie_pk>/recommend/', views.movies_recommend),
    path('<int:movie_pk>/like_recommend/', views.like_movie_recommend),
    path('actors/<actor_name>/', views.actors_detail),
    path('like_movie/<int:movie_pk>/', views.like_movie),
    path('like_actor/<int:actor_pk>/', views.like_actor),
    path('watch_movie/<int:movie_pk>/', views.watch_movie),
    path('search/',views.search),
    path('genres/', views.genre_list),
    path('genres/<int:genre_id>/', views.genre_movie),
    path('random_movie/', views.random_movie)
]