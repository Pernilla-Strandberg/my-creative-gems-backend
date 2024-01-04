from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsPostOrCommentOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow access only to post or comment owners.
    If comment is private, allow access only to post owner and comment owner.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is the owner of the post or comment
        is_post_owner = request.user == obj.post.owner
        is_comment_owner = request.user == obj.owner
        is_private_comment = obj.is_private

        return is_post_owner or (is_comment_owner and not is_private_comment)
