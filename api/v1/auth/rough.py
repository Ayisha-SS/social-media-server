# import json
# import requests

# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated,AllowAny
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.hashers import make_password

# from posts.models import ViewPost


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def create(request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     name = request.data.get('name')

#     print('email', email)
#     print('password', password)
#     print('name', name)

#     if not all([email, password, name]):
#         response_data = {
#             "status_code": 6002,
#             "data": "Missing required fields",
#             "message": "Please provide all required fields"
#         }
#         return Response(response_data, status=400)


#     if not User.objects.filter(username=email).exists():
#         user = User.objects.create_user(
#             username=email,
#             email=email,
#              password=make_password(password),
#             # password=password,
#             first_name=name,
#             is_active=True
#         )

#         refresh = RefreshToken.for_user(user)
#         token_data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }

#         response_data = {
#             "status_code": 6000,
#             "data": token_data,
#             "message": "Account created"
#         }
#     else:
#         response_data = {
#             "status_code": 6001,
#             "data": "User already exists"
#         }

#     return Response(response_data, status=200)


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def token_view(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     user = authenticate(email=email, password=password)
#     if user is not None:
#         login(request, user)
#         refresh = RefreshToken.for_user(user)
#         token_data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }
#         return Response(token_data, status=200)
#     else:
#         return Response({'error': 'Invalid credentials'}, status=400)



# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.hashers import make_password
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.decorators import api_view, permission_classes
# from posts.models import Signup, LogIn

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def signup(request):
#     username = request.data.get('username')
#     email = request.data.get('email')
#     password = request.data.get('password')

#     if not all([username, email, password]):
#         return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

#     if Signup.objects.filter(username=username).exists():
#         return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

#     signup_user = Signup(username=username, email=email, password=make_password(password))
#     signup_user.save()

#     login_user = LogIn(username=email, password=make_password(password))
#     login_user.save()

#     return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     login_user = LogIn.objects.filter(username=username, password=password).first()
#     if login_user:
#         refresh = RefreshToken.for_user(login_user)
#         token_data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }
#         return Response(token_data, status=status.HTTP_200_OK)
#     else:
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)





# @api_view(['POST'])
# @permission_classes([AllowAny])
# def signup(request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     name = request.data.get('name')

#     if not all([email, password, name]):
#         return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

#     if User.objects.filter(username=email).exists():
#         return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

#     user = User.objects.create_user(
#         username=email,
#         email=email,
#         # password=make_password(password),
#         password=password,
#         first_name=name,
#         is_active=True
#     )

#     refresh = RefreshToken.for_user(user)
#     token_data = {
#     'refresh': str(refresh),
#     'access': str(refresh.access_token)
#   }

#     return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     user = authenticate(email=email, password=password)
#     if user is not None:
#         login(request, user)
#         refresh = RefreshToken.for_user(user)
#         token_data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token)
#         }
#         print(user.is_active)
#         return Response(token_data, status=status.HTTP_200_OK)
#     else:
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def logout_view(request):
#     refresh_token = RefreshToken(request.data.get('refresh_token'))
#     refresh_token.blacklist()
#     return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)






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