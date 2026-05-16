from rest_framework import serializers

from .models import Post
from ..tags.models import Tag
from ..categories.models import Category
from ..comments.serializers import CommentReadSerializer


class PostReadSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    comments = CommentReadSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'image_url', 'user', 'category', 'tags', 'comments', 'created_at', 'updated_at'
        ]

        read_only_fields = [
            'id', 'user', 'created_at', 'updated_at'
        ]

class PostWriteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'image_url', 'user', 'category', 'tags', 'created_at', 'updated_at'
        ]

        read_only_fields = [
            'id', 'user', 'created_at', 'updated_at'
        ]
