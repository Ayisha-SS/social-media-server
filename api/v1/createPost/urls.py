from django.urls import path
from api.v1.createPost import views


urlpatterns = [
    path('createpost/',views.create_post),
    path('createpost/view/<int:pk>/',views.view_post),
]