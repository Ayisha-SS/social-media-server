from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'content', 'created_at', 'updated_at']