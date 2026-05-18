from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse

from .models import Category
from .serializers import CategorySerializer
from ..posts.serializers import PostReadSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


@extend_schema_view(
    list=extend_schema(
        tags=["Categories"],
        summary="Список категорий",
        description="Возвращает список всех категорий, отсортированных по имени.",
        responses={200: CategorySerializer(many=True)}
    ),
    retrieve=extend_schema(
        tags=["Categories"],
        summary="Получить категорию",
        description="Возвращает одну категорию по ID.",
        responses={200: CategorySerializer}
    ),
    posts=extend_schema(
        tags=["Categories"],
        summary="Получить посты по категории",
        description="Возвращает список всех публикаций, которые относятся к данной категории.",
        responses={200: PostReadSerializer(many=True)}
    )
)
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    ordering = ['name']
    
    @action(detail=True, methods=['GET'])
    def posts(self, request, pk=None):
        category = self.get_object() 
        posts = category.posts.all()
        
        serializer = PostReadSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)