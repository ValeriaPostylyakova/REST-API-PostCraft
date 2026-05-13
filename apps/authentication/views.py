from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (RegisterSerializer, LoginSerializer, UserSerializer)
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
@permission_classes([AllowAny])

def register(request):
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


@api_view(['POST'])
@permission_classes([AllowAny])

def login(request):
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])

def logout(request):
	try:
		refresh = request.data.get('refresh')
		RefreshToken(refresh).blacklist()

		return Response({
		'message': "Вы успешно вышли из системы."
		}, status=status.HTTP_200_OK)
	
	except Exception:
		return Response({'error': 'Невалидный токен. Пожалуйста, повторите попытку.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
	serializer = UserSerializer(request.user)
	return Response(serializer.data, status=status.HTTP_200_OK)
