from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import CreatePost

class CreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = CreatePost
        fields = ("id",'title','image','category','description','created_at')

    def create(self, validated_data):
        return CreatePost.objects.create(**validated_data)




   