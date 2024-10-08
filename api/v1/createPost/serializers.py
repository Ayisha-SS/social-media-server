from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import CreatePost, ViewPost

class CreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    def get_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)

    class Meta:
        model = CreatePost
        fields = ('id','title','image','category','description','created_at','created_by')

    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return CreatePost.objects.create(**validated_data)
    

class PostViewSerializer(ModelSerializer):


    class Meta:
        fields = ("id",'title','image','category','created_by','description')
        model = CreatePost

    