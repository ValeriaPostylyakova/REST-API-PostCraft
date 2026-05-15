from rest_framework import serializers
from .models import Post

from ..authentication.serializers import UserSerializer
from ..tags.serializers import TagSerializer
from ..categories.serializers import CategorySerializer

from django.contrib.auth.models import User
from ..tags.models import Tag
from ..categories.models import Category
from ..comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(
        read_only=True
    )

    tags = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    tag_ids = serializers.PrimaryKeyRelatedField(

        queryset=Tag.objects.all(),

        many=True,

        source='tags',

        write_only=True
    )

    category = serializers.StringRelatedField(
        read_only=True
    )

    category_id = serializers.PrimaryKeyRelatedField(

        queryset=Category.objects.all(),

        source='category',

        write_only=True
    )

    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:

        model = Post

        fields = [

            'id',

            'title',

            'content',

            'user',

            'category',

            'category_id',

            'tags',

            'tag_ids',

            'comments',

            'created_at',

            'updated_at'
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at'
        ]
