from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse

from .serializers import CommentReadSerializer, CommentWriteSerializer
from .models import Comment
from ..posts.permissions import IsAuthorOrReadOnly


@extend_schema_view(
    list=extend_schema(
        tags=["Comments"],
        summary="Список комментариев",
        description="Возвращает список всех комментариев с пользователем и постом.",
        responses={200: CommentReadSerializer(many=True)}
    ),

    retrieve=extend_schema(
        tags=["Comments"],
        summary="Получить комментарий",
        description="Возвращает один комментарий по ID.",
        responses={200: CommentReadSerializer}
    ),

    create=extend_schema(
        tags=["Comments"],
        summary="Создать комментарий",
        description="Создаёт комментарий для поста (требуется авторизация).",
        request=CommentWriteSerializer,
        responses={201: CommentReadSerializer}
    ),

    update=extend_schema(
        tags=["Comments"],
        summary="Обновить комментарий",
        description="Полное/частичное обновление комментария (только автор).",
        request=CommentWriteSerializer,
        responses={200: CommentReadSerializer}
    ),

    partial_update=extend_schema(
        tags=["Comments"],
        summary="Частичное обновление комментария",
        request=CommentWriteSerializer,
        responses={200: CommentReadSerializer}
    ),

    destroy=extend_schema(
        tags=["Comments"],
        summary="Удалить комментарий",
        description="Удаление комментария (только автор).",
        responses={204: OpenApiResponse(description="Комментарий удалён")}
    ),
)
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.select_related('user', 'post')
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CommentWriteSerializer
        return CommentReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment = serializer.save(user=request.user)

        response_serializer = CommentReadSerializer(
            comment,
            context={'request': request}
        )

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        comment = serializer.save()

        response_serializer = CommentReadSerializer(
            comment,
            context={'request': request}
        )

        return Response(response_serializer.data, status=status.HTTP_200_OK)