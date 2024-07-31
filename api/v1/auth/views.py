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
from . serializers import UserCreateSerializer, UserSerializers


@api_view(['GET'])
@permission_classes([AllowAny])
def show(request):
    instance = User.objects.all()
    serializer = UserSerializers(instance, many=True)
    response_data={
        "status_code":6000,
        "data":serializer.data
    }
    return Response(response_data)


@api_view(['POST'])
@permission_classes([AllowAny])
def profile(request):
    username = request.data['username']

    instance = User.objects.get(username=username)

    context = {
        request:"request"
    }
    serializer = UserSerializers(instance, context=context)
    response_data={
        "status_code":6000,
        "data":serializer.data
    }
    return Response(response_data)




@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):
    username = request.data.get('username')
    email = request.data.get('email')
    role = request.data.get('role')
    password = request.data.get('password')

    if not all([username, email, role, password]):
        response_data = {
            "status_code": 6001,
            "message": "Missing required fields"
        }
        return Response(response_data, status=400)

    if User.objects.filter(username=username).exists():
        response_data = {
            "message": "username already exist"
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        response_data = {
            "status_code": 6001,
            "message": "email already exist"
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
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response_data = {
            "status_code": 6000,
            "message": "User created Sucessfully",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "role": user.role
        }
        return Response(response_data, status=201)
    else:
        response_data = {
            "status_code": 6001,
            "data": serializer.errors
        }
        return Response(response_data, status=400)


    
