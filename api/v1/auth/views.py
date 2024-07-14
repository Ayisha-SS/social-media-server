import json
import requests

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from posts.models import ViewPost


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def create(request):

#     email = request.data.get('email')
#     password = request.data.get('password')
#     name = request.data.get('name')

#     print('email',email)
#     print('password',password)
#     print('name',name)

#     if not User.objects.filter(username=email).exists():

#         user = User.objects.create_user(
#             username=email,
#             password=password,
#             first_name=name
#         )

#         headers = {
#             "Content-Type":"application/json"
#         }

#         # data = f"'username':'{email}','password:'{password}'"
#         # final_data = "{" + data + "}"
#         token_data ={
#             'username':email,
#             'password':password
#         }

#         token_url = request.build_absolute_uri('/api/v1/auth/token/')
#         response = requests.post(token_url, headers={"Content-Type": "application/json"}, data=json.dumps(token_data))


#         protocol = "http://"
#         if request.is_secure():
#             protocol="https://"

#         host = request.get_host()

#         url = protocol+ host +"/api/v1/auth/create/"

#         response = requests.post(url,headers=headers, data=json.dumps(token_data))

#         if response.status_code == 200:

#             response_data = {
#                 "status_code":6000,
#                 "data":response.json(),
#                 "message":"Account created"
#             }
#         else:
#             response_data = {
#                 "status_code":6001,
#                 "data":"An error occured"
#         }
#     else:
#         response_data = {
#             "status_code":6001,
#             "data":"User already exists"
#         }
         
#     return Response(response_data,status=response.status_code)



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


    