import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

from posts.models import User
from . serializers import UserCreateSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):
    username = request.data.get('username')
    email = request.data.get('email')
    role = request.data.get('role')
    password = request.data.get('password')
    username = email
    
    print("*"*50)
    print(username)
    print("*"*50)

    if User.objects.filter(username=username).exists():
        response_data={
            "message":"username already exist"
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(email=email).exists():
        response_data={
            "status_code":6001,
            "message":"email already exist"
        }
        return Response(response_data)
    
    data = {
        'username': username,
        'email': email,
        'role': role,
        'password': password
    }
    serializer = UserCreateSerializer(data=data)
    if serializer.is_valid():
        # serializer.save()
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response_data={
            "status_code":6000,
            "message":"User created Sucessfully",
            "access":str(refresh.access_token),
            "refresh": str(refresh),
            "role":user.role

        }
        return Response(response_data, status=201)
    else:
        response_data={
            "status_code":6001,
            "data":serializer.errors
        }
        return Response(response_data, status=400)



