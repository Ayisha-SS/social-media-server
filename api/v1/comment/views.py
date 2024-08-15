from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from posts.models import Comment
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CommentSerializer



# class CreateCommentView(APIView):
#     def post(self, request):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    
class CreateCommentView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['created_by'] = request.user.username  # Assuming you're using username as created_by
        
        serializer = CommentSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostCommentsView(APIView):
    def get(self, request, post_id):
        comments = Comment.objects.filter(object_id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)