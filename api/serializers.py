from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """   
    Serializer for Django User model, including id, username, and email fields.    
    """
    
    
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']