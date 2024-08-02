from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.v1.createPost.serializers import CreateSerializer, CreateViewSerializer
from django.shortcuts import get_object_or_404
from api.v1.posts.serializers import PostViewSerializer
from posts.models import CreatePost
from posts.models import User
from posts.models import ViewPost 
 
from django.http import JsonResponse

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])

def create_post(request):
    
    if request.method == 'GET':
        posts = CreatePost.objects.all()  
        # posts = CreatePost.objects.filter(created_by=request.user)
        serializer = CreateSerializer(posts, many=True,context={'request': request})  
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
            

        
        serializer = CreateSerializer(data=request.data,context={'request': request})
           
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def view_post(request, id):
#     post = get_object_or_404(CreatePost, id=id)
#     serializer = CreateSerializer(post, context={'request': request})
#     return Response({'status_code': 200, 'data': serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def Viewposts(request,pk):

    if ViewPost.objects.filter(pk=pk).exists():
        instances = ViewPost.objects.get(pk=pk)
        context = {
            "request":request
        }
        serializer = CreateViewSerializer(instances,context = context)
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
    


def delete_null_created_by(request):
        if request.method == 'DELETE':
        # Filter and delete items where created_by is null
            deleted_count, _ = CreatePost.objects.filter(created_by__isnull=True).delete()
            return JsonResponse({'message': f'{deleted_count} items deleted.'})
        else:
            return JsonResponse({'error': 'Invalid request method.'}, status=400)
