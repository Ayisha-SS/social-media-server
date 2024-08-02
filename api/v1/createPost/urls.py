from django.urls import path
from api.v1.createPost import views
# from api.v1.posts.views import post


urlpatterns = [
    path('createpost/',views.create_post),
    path('view/<int:pk>/',views.Viewposts),

    path('api/v1/createpost/delete_null/', views.delete_null_created_by, name='delete_null_created_by'),
]