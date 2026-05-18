from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'avatar']

    def validate_avatar(value):
        if not value:
            return value

        allowed_extensions = ('.jpg', '.png', '.jpeg')
        if not value.name.lower().endswith(allowed_extensions):
            raise serializers.ValidationError(
                "Недопустимое расширение изображения. Загрузите другое изображение и попробуйте ещё раз."
            )

        if value.size > 1024 * 1024:
            raise serializers.ValidationError("Размер изображения не должен превышать 1МБ")

        return value
