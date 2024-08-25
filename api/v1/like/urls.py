from django.urls import path
from .views import LikePostView


urlpatterns = [
    path('like/', LikePostView.as_view(), name='like-post'),
]