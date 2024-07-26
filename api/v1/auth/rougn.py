# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.permissions import AllowAny
# from rest_framework.decorators import api_view,permission_classes



# @api_view(['POST'])
# @permission_classes([AllowAny])
# def create(request):

#     email = request.data['email']
#     password = request.data['password']
#     username = request.data['username']
#     userRole = request.data['userRole']


#     if not User.objects.filter(username=email).exists():

#         user = User.objects.create_user(
#             username=email,
#             password=password,
#             first_name=username,
#             # extra_fields={'userRole': userRole}  # Store userRole as an extra field
#         )
#         user.profile.userRole = userRole
#         user.save()

#         headers = {
#             "Content-Type":"application/json"
#         }

#         data = f'"username":"{email}","password":"{password}"'
#         final_data = "{" + data + "}"


#         protocol = "http://"
#         if request.is_secure():
#             protocol = "https://"

#         host = request.get_host()

#         url = protocol + host + "/api/v1/auth/token/"

#         response = requests.post(url,headers=headers,data=final_data)

#         if response.status_code == 200:

#             response_data = {
#                 "status_code":201,
#                 "data":response.json(),
#                 # "message":"Account created"
#                 "message": {
#                     "code": 6000,
#                     "message": "Account created successfully"
#                 },
#                  "userRole": userRole 
#             }

#         else:
#              response_data = {
#             "status_code":400,
#             # "data":"An error occured"
#             "message": {
#                     "code": 6001,
#                     "message": "An error occurred while creating the account"
#                 }
#         }
#     else:
#         response_data = {
#             "status_code":400,
#             # "data":"User exists"
#             "message": {
#                 "code": 6001,
#                 "message": "User already exists"
#             }
#         }

#     return Response(response_data,status=response_data["status_code"])