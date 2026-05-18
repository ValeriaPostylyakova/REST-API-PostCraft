from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.users.permissions import IsSuperUser
from django.contrib.auth.models import User

from ..posts.serializers import PostReadSerializer
from .serializers import UserSerializer

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view


User = get_user_model()

@extend_schema_view(
    list=extend_schema(
        tags=["Users"],
        summary="Получить список пользователей",
        description="Возвращает список всех пользователей. Доступно только суперпользователям.",
        responses={200: UserSerializer(many=True)},
    )
)



class UserViewSet(ViewSet):
    
    def get_permissions(self):
        if self.action == 'list':
            return [IsSuperUser()]
        return super().get_permissions()
    
    def list(self, request):
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)
    
    @extend_schema(
        tags=["Users"],
        summary="Получить посты пользователя",
        description="Возвращает список всех публикаций конкретного пользователя по его ID.",
        responses={200: PostReadSerializer(many=True)},
    )
    @action(detail=True, methods=['GET'])
    def posts(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = PostReadSerializer(user.posts.all(), many=True, context={'request': request})
        return Response(serializer.data)