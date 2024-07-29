import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token

from posts.models import User
from . serializers import UserSerializers , UserCreateSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):
    username = request.data.get('username')
    email = request.data.get('email')
    role = request.data.get('role')
    password = request.data.get('password')
    # username = email
    
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
        serializer.save()
        response_data={
            "status_code":6000,
            "message":"User created Sucessfully"

        }
        return Response(response_data, status=201)
    else:
        response_data={
            "status_code":6001,
            "data":serializer.errors
        }
        return Response(response_data, status=400)



# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not email or not password:
#             return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

#         user = authenticate(username=email, password=password)


#         if not user:
#             return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#         token, created = Token.objects.get_or_create(user=user)

#         return Response({
#             'token': token.key,
#             'role': user.role
#         }, status=status.HTTP_200_OK)