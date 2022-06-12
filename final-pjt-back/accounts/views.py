from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.http import require_POST
from .serializers import ProfileSerializer
from django.http import JsonResponse
User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)



# @require_POST
# def follow(request, user_pk):
#     if request.user.is_authenticated:
#         person = get_object_or_404(get_user_model(), pk=user_pk)
#         user = request.user
#         if person != user:
#             if person.followers.filter(pk=user.pk).exists():
#                 person.followers.remove(user)
#                 followed = False
#             else:
#                 person.followers.add(user)
#                 followed = True
#             follow_status = {
#                 'followers_count': person.followers.count(),
#                 'followings_count': person.followings.count(),
#                 'followed': followed,
#             }
#             return JsonResponse(follow_status)
#     return redirect('accounts:profile', person.username)

