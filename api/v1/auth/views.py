# import json
# import requests

# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated,AllowAny
# # from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User

# from posts.models import ViewPost


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def create(request):

#     email = request.data['email']
#     password = request.data['password']
#     name = request.data['name']

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

import json
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        name = request.data.get('name')

        if not email or not password or not name:
            return Response({"error": "Email, password, and name are required."}, status=400)

        if User.objects.filter(username=email).exists():
            return Response({"error": "User already exists."}, status=400)

        user = User.objects.create_user(username=email, password=password, first_name=name)

        # Assuming you want to immediately authenticate the user and obtain a token
        token_data = {
            'username': email,
            'password': password
        }

        # Assuming /api/v1/auth/token/ is the endpoint for token generation
        token_url = request.build_absolute_uri('/api/v1/auth/token/')
        response = requests.post(token_url, headers={"Content-Type": "application/json"}, data=json.dumps(token_data))

        if response.status_code == 200:
            response_data = {
                "status_code": 6000,
                "data": response.json(),
                "message": "Account created successfully."
            }
        else:
            response_data = {
                "status_code": 6001,
                "data": "An error occurred while fetching token."
            }

        return Response(response_data, status=response.status_code)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
