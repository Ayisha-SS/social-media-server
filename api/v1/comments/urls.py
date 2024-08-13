from django.urls import path
# from rest_framework.routers import DefaultRouter
from .views import add_comment

# router = DefaultRouter()
# router.register(r'comments', CommentViewSet)

# urlpatterns = [
#     path('comments/', include(router.urls)),
# ]

urlpatterns = [
    path('comments/', add_comment, name='add_comment'),
]