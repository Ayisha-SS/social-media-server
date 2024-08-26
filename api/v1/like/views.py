
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Like, User, CreatePost, ViewPost

class LikePostView(APIView):
    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        user_id = request.data.get('user_id')

        
        if not post_id or not user_id:
            return Response({"error": "post_id and user_id are required."}, status=status.HTTP_400_BAD_REQUEST)

        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        #
        post = None
        try:
            post = CreatePost.objects.get(id=post_id)
        except CreatePost.DoesNotExist:
            try:
                post = ViewPost.objects.get(id=post_id)
            except ViewPost.DoesNotExist:
                return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        
        existing_like = Like.objects.filter(object_id=post.id, user=user).first()
        if existing_like:
            
            existing_like.delete()
            message = "Post unliked."
            status_code = status.HTTP_200_OK
        else:
           
            Like.objects.create(content_object=post, user=user)
            message = "Post liked."
            status_code = status.HTTP_201_CREATED

        
        like_count = Like.objects.filter(object_id=post.id).count()

        return Response({"message": message, "like_count": like_count}, status=status_code)
