
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from posts.models import Like, User, CreatePost, ViewPost
from .serializers import LikeSerializer


class LikePostView(APIView):
    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        content_type_id = request.data.get('content_type_id')
        user_id = request.data.get('user_id')  

        
        if not post_id or not content_type_id or not user_id:
            return Response({"error": "post_id, content_type_id, and user_id are required."}, status=status.HTTP_400_BAD_REQUEST)

       
        try:
            content_type = ContentType.objects.get_for_id(content_type_id)
        except ContentType.DoesNotExist:
            return Response({"error": "Invalid content type ID."}, status=status.HTTP_400_BAD_REQUEST)

        
        model_class = content_type.model_class()
        if model_class is None:
            return Response({"error": "Model class not found for the content type ID."}, status=status.HTTP_400_BAD_REQUEST)

        
        try:
            post = model_class.objects.get(id=post_id)
        except model_class.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        
        existing_like = Like.objects.filter(content_type=content_type, object_id=post.id, user=user).first()
        if existing_like:
            
            existing_like.delete()
            message = "Post unliked."
            status_code = status.HTTP_200_OK
        else:
           
            Like.objects.create(content_type=content_type, object_id=post.id, user=user)
            message = "Post liked."
            status_code = status.HTTP_201_CREATED

        
        like_count = post.get_like_count()

        return Response({"message": message, "like_count": like_count}, status=status_code)