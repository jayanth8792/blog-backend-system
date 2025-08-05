from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Blog
from .serializers import BlogSerializer, BlogCreateSerializer

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.filter(published=True)
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = Blog.objects.filter(published=True)
        author_id = self.request.query_params.get('author', None)
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, published=True)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Blog.objects.filter(published=True)
    
    def update(self, request, *args, **kwargs):
        blog = self.get_object()
        if blog.author != request.user:
            return Response({'error': 'You do not have permission to edit this blog'}, 
                          status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        blog = self.get_object()
        if blog.author != request.user:
            return Response({'error': 'You do not have permission to delete this blog'}, 
                          status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    serializer = BlogCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def blog_comments(request, blog_id):
    from comments.models import Comment
    from comments.serializers import CommentSerializer
    
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(blog=blog, parent=None)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
