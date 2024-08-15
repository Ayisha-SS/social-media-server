from django.urls import path
from api.v1.createPost import views
# from api.v1.posts.views import post
from api.v1.createPost.views import DeletePostView, post_detail


urlpatterns = [
    path('createpost/',views.create_post),
    path('createpost/<int:pk>/',  DeletePostView.as_view()),
    # path('createpost/view/<int:pk>/',views.post),
    path('<str:model_name>/view/<int:pk>/', post_detail), 
]