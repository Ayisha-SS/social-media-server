from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User




# User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    # created_by = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'content', 'created_at', 'updated_at','created_by']

        # def get_created_by(self, obj):
        # # Ensure that created_by is a User instance and has a username
        #     if obj.created_by:
        #         return obj.created_by.username
        #     return None