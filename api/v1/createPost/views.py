from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from api.v1.createPost.serializers import CreateSerializer
from posts.models import CreatePost
from api.v1.createPost.serializers import ViewSerializer
 

@api_view(['GET', 'POST','DELETE'])
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
        


class DeletePostView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            post = CreatePost.objects.get(pk=pk)
        except CreatePost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostDetailView(generics.RetrieveAPIView):
    queryset = CreatePost.objects.all()
    serializer_class = ViewSerializer



    


