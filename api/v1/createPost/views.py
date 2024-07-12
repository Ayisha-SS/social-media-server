from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from api.v1.createPost.serializers import CreateSerializer 
from posts.models import ViewPost,CreatePost


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def create_post(request):
#     context = {
#         "request": request
#     }
#     print("Request data:", request.data)
#     serializer = CreateSerializer(data=request.data, context=context)
#     if serializer.is_valid():
#         serializer.save()
#         response_data = {
#             "status_code": 6000,
#             "message": "Post created successfully",
#             "data": serializer.data
#         }
#         return Response(response_data, status=status.HTTP_201_CREATED)
#     print("Serializer errors:", serializer.errors)
#     response_data = {
#         "status_code": 4000,
#         "message": "Post creation failed",
#         "errors": serializer.errors
#     }
#     return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST', 'OPTIONS'])
# @permission_classes([AllowAny])
# def create_post(request):
#     if request.method == 'POST':
#         context = {"request": request}
#         serializer = CreateSerializer(data=request.data, context=context)
#         if serializer.is_valid():
#             serializer.save()
#             response_data = {
#                 "status_code": 6000,
#                 "message": "Post created successfully",
#                 "data": serializer.data
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         response_data = {
#             "status_code": 4000,
#             "message": "Post creation failed",
#             "errors": serializer.errors
#         }
#         return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'OPTIONS':
#         # Handle OPTIONS request if necessary (e.g., CORS preflight)
#         return Response(status=status.HTTP_200_OK)
    

# @api_view(['GET'])
# @permission_classes([AllowAny])  # Adjust permission classes as needed
# def posts(request):
#     try:
#         instances = ViewPost.objects.filter(is_deleted=False)
#         serializer = PostSerializer(instances, many=True)
#         response_data = {
#             "status_code": 200,
#             "data": serializer.data
#         }
#         return Response(response_data)
#     except Exception as e:
#         response_data = {
#             "status_code": 500,
#             "error": str(e)
#         }
#         return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET', 'POST','DELETE'])
@permission_classes([AllowAny])  # Adjust permission classes as needed
def create_post(request):
    if request.method == 'GET':
        # Handle GET request to fetch all posts
        posts = CreatePost.objects.all()  # Example filter condition
        serializer = CreateSerializer(posts, many=True,context={'request': request})  # Use serializer to serialize queryset
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Handle POST request to create a new post
        try:
            serializer = CreateSerializer(data=request.data,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        # Handle DELETE request to delete a post
        try:
            post_id = request.query_params.get('id')  # Assuming you pass id as a query parameter
            post = CreatePost.objects.get(id=post_id)
            post.delete()
            return Response({"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        # except CreatePost.DoesNotExist:
        #     return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)