import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,permission_classes




@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):

    email = request.data['email']
    password = request.data['password']
    username = request.data['username']
    role = request.data['role']


    if not User.objects.filter(username=email).exists():

        User.objects.create_user(
            username=email,
            password=password,
            first_name=username
        )

        headers = {
            "Content-Type":"application/json"
        }

        data = f'"username":"{email}","password":"{password}","role":"{role}"'
        final_data = "{" + data + "}"


        protocol = "http://"
        if request.is_secure():
            protocol = "https://"

        host = request.get_host()

        url = protocol + host + "/api/v1/auth/token/"

        response = requests.post(url,headers=headers,data=final_data)

        if response.status_code == 200:

            response_data = {
                "status_code":201,
                "data":response.json(),
                "message":"Account created"
            }

        else:
             response_data = {
            "status_code":400,
            "data":"An error occured"
        }
    else:
        response_data = {
            "status_code":400,
            "data":"User exists"
        }

    return Response(response_data,status=response_data["status_code"])