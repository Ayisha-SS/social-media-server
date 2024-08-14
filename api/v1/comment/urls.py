from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.CreateCommentView.as_view()),
    path('comments/<int:post_id>/', views.PostCommentsView.as_view()),
]