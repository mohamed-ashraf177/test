from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .serializers import UserSerializer



@api_view(['GET'])
def users_list(request):
    
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    
    
    
@api_view(['POST'])
def create_user(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
