from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Comment, CreatePost
from .serializers import CommentSerializer
from django.contrib.contenttypes.models import ContentType




@api_view(['POST'])
def add_comment(request):
    content_type_id = request.data.get('content_type')
    object_id = request.data.get('object_id')
    
    # Ensure the content_type is valid
    try:
        content_type = ContentType.objects.get_for_id(content_type_id)
    except ContentType.DoesNotExist:
        return Response({"content_type": ["Invalid content type."]}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create comment data
    data = {
        'content_type': content_type_id,
        'object_id': object_id,
        'author': request.user.id,
        'content': request.data.get('content')
    }
    
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_comments(request, object_id):
    # Assuming content_type ID for CreatePost is 1
    content_type_id = ContentType.objects.get_for_model(CreatePost).id
    
    comments = Comment.objects.filter(content_type=content_type_id, object_id=object_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)