from django.urls import path
from api.v1.createPost import views
# from api.v1.posts.views import post
from api.v1.createPost.views import PostDetailView


urlpatterns = [
    path('createpost/',views.create_post),
    path('view/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
]