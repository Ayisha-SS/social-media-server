from django.urls import path
from .views import contenttype_view

urlpatterns = [
    # other url patterns
    path('contenttype/', contenttype_view, name='contenttype_view'),
]