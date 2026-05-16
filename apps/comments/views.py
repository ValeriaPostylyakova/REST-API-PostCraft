from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CommentReadSerializer, CommentWriteSerializer
from .models import Comment

from ..posts.permissions import IsAuthorOrReadOnly

from rest_framework.response import Response
from rest_framework import status



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

			response_serializer = CommentReadSerializer(comment, context={'request': request})
			return Response(response_serializer.data, status=status.HTTP_201_CREATED)
		
		def update(self, request, *args, **kwargs):
			
			instanse = self.get_object()
			serializer = self.get_serializer(instanse, data=request.data, partial=True)
			serializer.is_valid(raise_exception=True)
			comment = serializer.save()

			response_serializer = CommentReadSerializer(comment, context={'request': request})
			return Response(response_serializer.data, status=status.HTTP_200_OK)
	