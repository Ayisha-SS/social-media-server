from rest_framework import serializers
from posts.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'author', 'content', 'created_at']
        # read_only_fields = ['id', 'author', 'created_at']  # Mark these fields as read-only

    # def create(self, validated_data):
    #     validated_data['author'] = self.context['request'].user  # Set the author field from the request
    #     return super().create(validated_data)
