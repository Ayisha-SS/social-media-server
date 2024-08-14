from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from posts.models import Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CommentSerializer



class CreateCommentView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
class PostCommentsView(APIView):
    def get(self, request, post_id):
        comments = Comment.objects.filter(object_id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)