from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.v1.createPost.serializers import CreateSerializer 
from django.shortcuts import get_object_or_404

from posts.models import CreatePost
from posts.models import User


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])

def create_post(request):
    
    if request.method == 'GET':
        posts = CreatePost.objects.all()  
        # posts = CreatePost.objects.filter(created_by=request.user)
        serializer = CreateSerializer(posts, many=True,context={'request': request})  
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
            
             # Extract the username from cookies
        # username = request.COOKIES.get('username')
        # if not username:
        #     return Response({'detail': 'Username not found in cookies.'}, status=status.HTTP_400_BAD_REQUEST)

        # # Get the user object
        # user = User.objects.filter(username=username).first()
        # if not user:
        #     return Response({'detail': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)

        # # Add the user to the request data
        # data = request.data.copy()
        # data['created_by'] = user.id
        
        serializer = CreateSerializer(data=request.data,context={'request': request})
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
