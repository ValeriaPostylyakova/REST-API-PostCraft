from rest_framework import serializers
from .models import Comment
from ..posts.models import Post
from ..authentication.serializers import UserSerializer


class CommentReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(
        read_only=True
    )

    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment

        fields = ['id', 'content', 'user', 'post', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'post', 'created_at', 'updated_at']

class CommentWriteSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        write_only=True
    )

    class Meta:
        model = Comment

        fields = ['id', 'content', 'user', 'post', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

