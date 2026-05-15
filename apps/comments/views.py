from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CommentSerializer
from .models import Comment

from ..posts.permissions import IsAuthorOrReadOnly



class CommentViewSet(ModelViewSet):
		queryset = Comment.objects.select_related('user', 'post')
		serializer_class = CommentSerializer
		permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
		
		def perform_create(self, serializer):
				serializer.save(user=self.request.user)
	