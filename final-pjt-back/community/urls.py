from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('popular_articles/', views.like_article_list),
    path('<int:movie_pk>/articles/', views.article_create),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('like_article/<int:article_pk>/', views.like_article),
    path('<int:article_pk>/comments/', views.article_comment_list),
]
