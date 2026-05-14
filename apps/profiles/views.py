from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):

	serializer = ProfileSerializer(request.user.profile)
	return Response(serializer.data, status=status.HTTP_200_OK)
	
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request):

	serializer = ProfileSerializer(request.user.profile, data=request.data, partial=True)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	
