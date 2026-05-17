from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.users.permissions import IsSuperUser
from django.contrib.auth.models import User

from ..posts.serializers import PostReadSerializer
from .serializers import UserSerializer

from django.shortcuts import get_object_or_404

class UserViewSet(ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            return [IsSuperUser()]
        return super().get_permissions()
    
    def list(self, request):
        
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)
    
    @action(detail=True, methods=['GET'])
    def posts(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        
        serializer = PostReadSerializer(user.posts.all(), many=True, context={'request': request})
        return Response(serializer.data)