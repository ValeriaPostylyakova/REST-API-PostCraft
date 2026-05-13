from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User

from ..authentication.serializers import UserSerializer
from ..posts.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):

	user = UserSerializer(read_only=True)
	post = PostSerializer(read_only=True)

	user_id = serializers.PrimaryKeyRelatedField(
		queryset=User.objects.all(),
		source='user',
		write_only=True
	)

	post_id = serializers.PrimaryKeyRelatedField(
		queryset=User.objects.all(),
		source='post',
		write_only=True
	)

	class Meta:
		model = Comment
		fields = ['id', 'content', 'created_at', 'updated_at', 'user', 'post', 'user_id', 'post_id' ]
		read_only_fields = ['id', 'created_at', 'updated_at']