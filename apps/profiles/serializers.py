from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from ..authentication.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'bio', 'avatar']