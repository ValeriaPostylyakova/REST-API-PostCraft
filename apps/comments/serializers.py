from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User
from ..posts.models import Post

class CommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(
        read_only=True
    )

    post_id = serializers.PrimaryKeyRelatedField(

        queryset=Post.objects.all(),

        source='post',

        write_only=True
    )

    class Meta:

        model = Comment

        fields = [

            'id',

            'content',

            'user',

            'post_id',

            'created_at',

            'updated_at'
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at'
        ]