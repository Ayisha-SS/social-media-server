from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import CreatePost

class CreateSerializer(ModelSerializer):

    class Meta:
        model = CreatePost
        fields = ("id",'title','image','category','created_at')

   


class CreateViewSerializer(ModelSerializer):

    class Meta:
        fields = ("id",'title','image','category','created_by','description','created_at')
        model = CreatePost

   