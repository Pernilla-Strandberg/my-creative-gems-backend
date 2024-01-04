from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List comments, create if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = Comment.objects.filter(
            models.Q(owner=user) | models.Q(recipient=user),
            is_private=True
        )
        return queryset


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/update/delete comment by own id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Comment.objects.filter(
            models.Q(owner=user) | models.Q(recipient=user),
            is_private=True,
            recipient__isnull=False
        )
        return queryset
