from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view
)

from .serializers import ProfileSerializer


@extend_schema_view(
    me=extend_schema(
        tags=["Profile"],
        summary="Мой профиль",
        description="Получение и обновление профиля текущего авторизованного пользователя.",
        responses={200: ProfileSerializer}
    )
)
class ProfileViewSet(ViewSet):

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):

        if request.method == 'GET':
            serializer = ProfileSerializer(request.user.profile)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'PATCH':
            serializer = ProfileSerializer(
                request.user.profile,
                data=request.data,
                partial=True
            )

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)