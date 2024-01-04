from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly, IsPostOrCommentOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer, PrivateCommentSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List all comments
    Create a new comment if authenticated
    Associate current logged-in user with the comment
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/update/delete comment by own id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()


class PrivateCommentList(generics.ListCreateAPIView):
    """
    List private comments for post owner and comment owner
    Create a new private comment if authenticated
    Associate the current logged-in user with the comment
    """
    permission_classes = [permissions.IsAuthenticated,
                          IsPostOrCommentOwnerOrReadOnly]
    serializer_class = PrivateCommentSerializer

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(is_private=True, post__owner=user) | Comment.objects.filter(is_private=True, owner=user)
