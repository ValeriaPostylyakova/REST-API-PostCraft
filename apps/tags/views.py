from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

from .serializers import TagSerializer
from .models import Tag

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ..posts.serializers import PostReadSerializer


@extend_schema_view(
    list=extend_schema(
        tags=["Tags"],
        summary="Список тегов",
        description="Возвращает список всех тегов, отсортированных по имени.",
        responses={200: TagSerializer(many=True)}
    ),
    retrieve=extend_schema(
        tags=["Tags"],
        summary="Получить тег",
        description="Возвращает один тег по ID.",
        responses={200: TagSerializer}
    ),
    # Документируем кастомный метод posts здесь
    posts=extend_schema(
        tags=["Tags"],
        summary="Получить посты по тегу",
        description="Возвращает список всех публикаций, к которым привязан данный тег.",
        responses={200: PostReadSerializer(many=True)}
    )
)
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    ordering = ['name']
    
    @action(detail=True, methods=['GET'])
    def posts(self, request, pk=None):
        tag = self.get_object() 
        posts = tag.posts.all()
        
        serializer = PostReadSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
       
        