from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ViewSet

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiResponse,
    OpenApiExample
)

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import RegisterSerializer, LoginSerializer
from ..users.serializers import UserSerializer






@extend_schema_view(
    register=extend_schema(
        tags=["Authorization"],
        summary="Регистрация пользователя",
        description="Создаёт нового пользователя и возвращает JWT токены.",
        request=RegisterSerializer,
        responses={
            201: OpenApiResponse(
                response=UserSerializer,
                description="Пользователь успешно создан"
            )
        },
        examples=[
            OpenApiExample(
                "Пример регистрации",
                value={
                    "username": "testuser",
                    "password": "strongpassword123"
                },
                request_only=True
            )
        ],
    ),

    login=extend_schema(
        tags=["Authorization"],
        summary="Вход пользователя",
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(
                response=UserSerializer,
                description="Успешный вход"
            )
        }
    ),

    logout=extend_schema(
        tags=["Authorization"],
        summary="Выход пользователя (blacklist refresh token)",
        request={
            "type": "object",
            "properties": {
                "refresh": {"type": "string"}
            }
        },
        responses={200: OpenApiResponse(description="Успешный выход")}
    ),

    me=extend_schema(
        tags=["Authorization"],
        summary="Получить или удалить текущего пользователя",
        responses={200: UserSerializer}
    ),
)
class AuthViewSet(ViewSet):
    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        try:
            refresh = request.data.get('refresh')
            RefreshToken(refresh).blacklist()

            return Response({"message": "Вы успешно вышли из системы."})

        except Exception:
            return Response(
                {"error": "Невалидный токен."},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['GET', 'DELETE'], permission_classes=[IsAuthenticated])
    def me(self, request):

        if request.method == 'GET':
            return Response(UserSerializer(request.user).data)

        if request.method == 'DELETE':
            try:
                refresh = request.data.get('refresh')
                RefreshToken(refresh).blacklist()
            except Exception:
                return Response(
                    {"error": "Невалидный токен."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            request.user.delete()
            return Response({"message": "User удалён."})
      
@extend_schema(
    tags=["Authorization"],
    summary="Обновление access токена",
    description="Принимает refresh token и возвращает новый access token",
)
class CustomTokenRefreshView(TokenRefreshView):
    pass



        