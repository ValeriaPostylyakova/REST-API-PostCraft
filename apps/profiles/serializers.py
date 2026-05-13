from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from ..authentication.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):

	user = UserSerializer(read_only=True)
	
	user_id = serializers.PrimaryKeyRelatedField(
		queryset=User.objects.all(),
		source='user',
		write_only=True
	)

	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'bio', 'avatar', 'user', 'user_id']