from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
    from blogs.models import Blog
    
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid():
        # Check if blog exists
        blog_id = request.data.get('blog')
        blog = get_object_or_404(Blog, id=blog_id)
        
        # Check if parent comment exists (if provided)
        parent_id = request.data.get('parent')
        if parent_id:
            parent = get_object_or_404(Comment, id=parent_id)
            if parent.parent is not None:
                return Response({'error': 'Cannot nest replies deeper than one level'},
                              status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(author=request.user)
        return Response(CommentSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return Response({'error': 'You do not have permission to edit this comment'}, 
                      status=status.HTTP_403_FORBIDDEN)
    
    serializer = CommentSerializer(comment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return Response({'error': 'You do not have permission to delete this comment'}, 
                      status=status.HTTP_403_FORBIDDEN)
    
    comment.delete()
    return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def comment_replies(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    replies = comment.replies.all()
    serializer = CommentSerializer(replies, many=True)
    return Response(serializer.data)
