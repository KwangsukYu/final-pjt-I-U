
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.comment import CommentSerializer, CommentListSerializer

from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Article, Comment
from rest_framework import status

from movies.models import Movie
from notifications.views import create_notification

@api_view(['GET'])
def article_list(request):
    articles = get_list_or_404(Article.objects.order_by('-pk'))
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def like_article_list(request):
    articles = get_list_or_404(Article.objects.order_by('-pk'))
    article_dict = {}
    for article in articles:
        article_dict[article] = article.article_users.count()
    article_dict=sorted(article_dict.items(), key=lambda x: x[1], reverse=True)
    article_list = []
    for key, _ in article_dict:
        article_list.append(key)
    serializer = ArticleListSerializer(article_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def article_create(request, movie_pk): 
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): 
        # serializer.save(movie=movie, user=request.user)
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    

    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'게시글 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
        
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save(article=article, user=request.user)
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_article(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    user = request.user
    if user.favorite_article.filter(pk=article_pk).exists():
        user.favorite_article.remove(article)
        data = 'remove'
        create_notification(user, article.user, 'unlike')
    else:
        user.favorite_article.add(article)
        data = 'add'
        create_notification(user, article.user, 'like')
    return Response({'data': data})


@api_view(['GET'])
def article_comment_list(request, article_pk):
    comments = Comment.objects.order_by('-created_at').filter(
        Q(article__id =article_pk)
    ).distinct()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)