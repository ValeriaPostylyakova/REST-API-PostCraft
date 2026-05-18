from rest_framework import serializers

from .models import Post
from ..tags.models import Tag
from ..categories.models import Category
from ..comments.serializers import CommentReadSerializer


class PostReadSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'image_url', 'user', 'category', 'tags','created_at', 'updated_at'
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
        
    def validate_image_url(self, value):
        if not value:
            return value

        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError('Размер изображения не должен превышать 5МБ')
        
        if not value.name.lower().endswith(('.jpg', '.png', '.jpeg')):
            raise serializers.ValidationError('Недопустимое расширение изображения. Загрузите другое изображение и попробуйте еще раз.')
        return value
