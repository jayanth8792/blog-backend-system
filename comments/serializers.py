from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ('id', 'blog', 'author', 'content', 'created_at', 'updated_at', 'parent', 'replies')
        read_only_fields = ('author', 'created_at', 'updated_at')
        
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []
        
    def validate_parent(self, value):
        if value and value.parent is not None:
            raise serializers.ValidationError("Cannot nest replies deeper than one level")
        return value

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('blog', 'content', 'parent')
        extra_kwargs = {
            'parent': {'required': False}
        }