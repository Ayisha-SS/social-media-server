from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import ViewPost

class PostSerializer(ModelSerializer):

    category = serializers.SerializerMethodField()

    class Meta:
        fields = ("id",'title','image','category','created_by')
        model = ViewPost

    def get_category(self,instance):
        return instance.category.name


class PostViewSerializer(ModelSerializer):

    category = serializers.SerializerMethodField()

    class Meta:
        fields = ("id",'title','image','category','created_by','description',"created_at")
        model = ViewPost

    def get_category(self,instance):
        return instance.category.name
    

