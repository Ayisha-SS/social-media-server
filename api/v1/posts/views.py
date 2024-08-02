from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from api.v1.posts.serializers import PostSerializer,PostViewSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import get_object_or_404

from posts.models import ViewPost

@api_view(["GET"])
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
@permission_classes([AllowAny])
def post(request, pk):
    instance = get_object_or_404(ViewPost, pk=pk)
    context = {
        "request": request
    }
    serializer = PostViewSerializer(instance, context=context)
    response_data = {
        "status_code": 200,
        "data": serializer.data
    }
    return Response(response_data)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
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
    
