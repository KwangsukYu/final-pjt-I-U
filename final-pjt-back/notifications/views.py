from django.shortcuts import render


from .models import Notification
from .serializer.notification import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Create your views here.


class Notification_cs(APIView):
    def get(self, request, format=None):
        user = request.user
        notifications = Notification.objects.filter(to=user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


def create_notification(creator, to, Notification_type):
    print(creator, to, Notification_type)

    notifications = Notification.objects.create(
        creator = creator,
        to = to,
        Notification_type = Notification_type,
    )
    notifications.save()