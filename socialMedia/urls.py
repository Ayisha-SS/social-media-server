
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/posts/',include('api.v1.posts.urls')),
    path('api/v1/',include('api.v1.createPost.urls')),
    path('api/v1/auth/',include('api.v1.auth.urls')),
    path('api/v1/',include('api.v1.comment.urls')),
    path('api/v1/',include('api.v1.contentType.urls'))
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
