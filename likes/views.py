from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    Display a list of likes or add a new like if user is logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Fetch a like based on its id and delete it if user are the owner.
    No need for RetrieveUpdate as likes do not require updates.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
