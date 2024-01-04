from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
# from django.shortcuts import get_object_or_404
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

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = Comment.objects.filter(
    #         models.Q(owner=user) | models.Q(recipient=user),
    #         is_private=True,
    #         post_id=self.kwargs['post_id'],  # Ensure correct filter. by post
    #     )
    #     return queryset


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/update/delete comment by own id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = Comment.objects.filter(
    #         models.Q(owner=user) | models.Q(recipient=user),
    #         is_private=True,
    #         recipient__isnull=False
    #     )
    #     return queryset

    # def get_object(self):
    #     queryset = self.get_queryset()
    #     obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
    #     self.check_object_permissions(self.request, obj)
    #     return obj
