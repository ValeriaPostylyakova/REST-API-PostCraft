from rest_framework.viewsets import (
    ModelViewSet
)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related(
        'user',
        'category'
    ).prefetch_related(
        'comments',
        'comments__user',
        'tags'
    )
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)