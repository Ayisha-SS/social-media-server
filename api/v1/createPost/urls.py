from django.urls import path
from api.v1.createPost import views
# from api.v1.posts.views import post
from api.v1.createPost.views import post, DeletePostView


urlpatterns = [
    path('createpost/',views.create_post),
    # path('view/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('createpost/view/<int:pk>/',post),
    path('createpost/view/<int:pk>/', views.createpost_detail, name='createpost_detail'),
    path('createpost/<int:pk>/',  DeletePostView.as_view())
]