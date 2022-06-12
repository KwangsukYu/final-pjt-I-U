from ..models import Notification
from rest_framework import serializers
from accounts.models import User
# from .movie import MovieSerializer


class NotificationSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('id','username')
    
    creator = UserSerializer()

    class Meta:
        model = Notification
        fields = '__all__'