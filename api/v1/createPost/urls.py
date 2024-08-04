from django.urls import path
from api.v1.createPost import views
# from api.v1.posts.views import post
from api.v1.createPost.views import PostDetailView, DeletePostView


urlpatterns = [
    path('createpost/',views.create_post),
    path('view/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('createpost/<int:pk>/',  DeletePostView.as_view())
]