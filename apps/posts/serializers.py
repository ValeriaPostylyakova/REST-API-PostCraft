from rest_framework import serializers
from .models import Post

from ..authentication.serializers import UserSerializer
from ..tags.serializers import TagSerializer
from ..categories.serializers import CategorySerializer

from django.contrib.auth.models import User
from ..tags.models import Tag
from ..categories.models import Category


class PostSerializer(serializers.ModelSerializer):

	user = UserSerializer(read_only=True)
	user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

	tags = TagSerializer(many=True, read_only=True)
	tag_ids = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, source='tags', write_only=True)

	category = CategorySerializer(read_only=True)
	category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

	class Meta:
		model = Post
		fields = ['id', 'title', 'content', 'user', 'user_id', 'category', 'tags', 'tag_ids', 'category_id', 'created_at', 'updated_at']
		read_only_fields = ['id', 'created_at', 'updated_at']
