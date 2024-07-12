from django.urls import path
from api.v1.posts import views


urlpatterns = [
    path('',views.posts ),
    path('view/<int:pk>/',views.post),
    path('protected/<int:pk>/',views.protected),
]