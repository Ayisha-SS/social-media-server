import json
import requests

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from posts.models import ViewPost


@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')

    print('email', email)
    print('password', password)
    print('name', name)

    if not User.objects.filter(username=email).exists():
        user = User.objects.create_user(
            username=email,
            password=password,
            first_name=name
        )

        refresh = RefreshToken.for_user(user)
        token_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        response_data = {
            "status_code": 6000,
            "data": token_data,
            "message": "Account created"
        }
    else:
        response_data = {
            "status_code": 6001,
            "data": "User already exists"
        }

    return Response(response_data, status=200)


