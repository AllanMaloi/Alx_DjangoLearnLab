from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification  # Import Notification model

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Ensure this field exists in CustomUser

        # Ensure the correct query structure
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


# ✅ Like a Post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)  # ✅ Using generics.get_object_or_404

    like, created = Like.objects.get_or_create(user=request.user, post=post)  # ✅ Using request.user explicitly

    if not created:
        return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    # ✅ Create a notification for the post author
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked",
        target=post
    )

    return Response({'message': 'Post liked successfully'}, status=status.HTTP_201_CREATED)


# ✅ Unlike a Post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)  # ✅ Using generics.get_object_or_404

    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
        like.delete()
        return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)

    return Response({'message': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)
