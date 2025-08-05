from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at', 'published', 'slug', 'comments_count')
        read_only_fields = ('author', 'created_at', 'updated_at')
        
    def get_comments_count(self, obj):
        return obj.comments.count()
        
    def validate_slug(self, value):
        if Blog.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Slug must be unique")
        return value

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'published', 'slug')
        extra_kwargs = {
            'slug': {'required': False}
        }
        
    def create(self, validated_data):
        # If slug is not provided, generate from title
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = validated_data['title'].lower().replace(' ', '-')
        return super().create(validated_data)