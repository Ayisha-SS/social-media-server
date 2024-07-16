from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.v1.createPost.serializers import CreateSerializer 
from django.shortcuts import get_object_or_404

from posts.models import CreatePost


@api_view(['GET', 'POST','DELETE'])
@permission_classes([IsAuthenticated])

def create_post(request):
    
    
    if request.method == 'GET':
        posts = CreatePost.objects.all()  
        serializer = CreateSerializer(posts, many=True,context={'request': request})  
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        
            serializer = CreateSerializer(data=request.data,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
       
        
    elif request.method == 'DELETE':
        
            post_id = request.query_params.get('id')  
            post = get_object_or_404(CreatePost, id=post_id)
            if post:
                post.delete()
                return Response({"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
    
    

#
    
