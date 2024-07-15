from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from api.v1.posts.serializers import PostSerializer,PostViewSerializer,CommentSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView

from posts.models import ViewPost,Comments

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def posts(request):
    context = {
        "request":request
    }
    
    instances = ViewPost.objects.filter(is_deleted=False)
    serializer = PostSerializer(instances,many=True,context = context)
    response_data = {
        "status_code":6000,
        "data":serializer.data
    }
    return Response(response_data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def post(request,pk):

    if ViewPost.objects.filter(pk=pk).exists():
        instances = ViewPost.objects.get(pk=pk)
        context = {
            "request":request
        }
        serializer = PostViewSerializer(instances,context = context)
        response_data = {
            "status_code":6000,
            "data":serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code":6001,
            "message":"No post founded"
        }
        return Response(response_data)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
# @permission_classes([AllowAny])
def protected(request,pk):

    if ViewPost.objects.filter(pk=pk).exists():
        instances = ViewPost.objects.get(pk=pk)
        context = {
            "request":request
        }
        serializer = PostViewSerializer(instances,context = context)
        response_data = {
            "status_code":6000,
            "data":serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code":6001,
            "message":"No post founded"
        }
        return Response(response_data)
    

class CreateCommentView(APIView):
    def post(self, request, pk):
        post = ViewPost.objects.get(pk=pk)
        comment = Comments(text=request.data['text'], post=post, created_by=request.user)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

