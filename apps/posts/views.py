from rest_framework.viewsets import (
    ModelViewSet
)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)

from .permissions import IsAuthorOrReadOnly
from .serializers import PostReadSerializer, PostWriteSerializer
from ..comments.serializers import CommentReadSerializer
from .models import Post

from rest_framework.response import Response
from rest_framework import status

from .pagination import PostPagination
from ..comments.pagination import CommentPagination

from rest_framework.filters import (
    SearchFilter, OrderingFilter
)

from rest_framework.decorators import action

from rest_framework.parsers import MultiPartParser, FormParser

class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related(
        'user',
        'category'
    ).prefetch_related(
        'comments',
        'comments__user',
        'tags'
    )
   
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    pagination_class = PostPagination

    filter_backends = [SearchFilter, OrderingFilter]

    parser_classes = [MultiPartParser, FormParser]

    search_fields = ['title', 'content', 'user__username', 'category__name', 'tags__name']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']

    def get_serializer_class(self):
       if self.action in ['create', 'update', 'partial_update']:
           return PostWriteSerializer
       return PostReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save(user=request.user)

        response_serializer = PostReadSerializer(post, context={'request': request})
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()

        response_serializer = PostReadSerializer(post, context={'request': request})
        return Response(response_serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.select_related('user').all()

        paginator = CommentPagination()
        page = paginator.paginate_queryset(comments, request)

        if page is not None:
            serializer = CommentReadSerializer(page, many=True, context={'request': request})
            return paginator.get_paginated_response(serializer.data)

        response_serializer = CommentReadSerializer(comments, many=True, context={'request': request})
        return Response(response_serializer.data, status=status.HTTP_200_OK)
