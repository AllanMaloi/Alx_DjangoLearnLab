from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikePostView, UnlikePostView
from .views import FeedView, UserFeedView
from .views import like_post, unlike_post


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('<int:pk>/like/', like_post, name='like_post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike_post'),

]
