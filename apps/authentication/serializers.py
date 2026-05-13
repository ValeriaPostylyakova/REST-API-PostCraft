from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from ..profiles.serializers import ProfileSerializer


class RegisterSerializer(serializers.ModelSerializer):

	password = serializers.CharField(write_only=True, min_length=8, max_length=30)
	confirm_password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'password', 'confirm_password']

	def validate_email(self, value):
		if User.objects.filter(email = value).exists():
			raise serializers.ValidationError("Пользователь с таким email уже существует. Войдите в аккаунт или используйте другую почту.")
		return value
	
	def validate(self, data):
		if data['password'] != data['confirm_password']:
			raise serializers.ValidationError("Пароли не совпадают. Пожалуйста, попробуйте ещё раз.")
		return data

	def create(self, validated_data):
		return User.objects.create_user(
			username=validated_data['username'],
			email=validated_data['email'],
			password=validated_data['password']
		)
	
class LoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(write_only=True)

	def validate(self, data):
		email = data.get('email')
		password = data.get('password')

		user = User.objects.filter(email=email).first()

		if user is None:
			raise serializers.ValidationError("Пользователь с таким email не существует. Пожалуйста, зарегистрируйтесь.")

		if not user.check_password(password):
			raise serializers.ValidationError("Неправильный пароль. Пожалуйста, попробуйте ещё раз.")

		user = authenticate(username=user.username, password=password)

		data['user'] = user

		return data

class UserSerializer(serializers.ModelSerializer):

	profile = ProfileSerializer(read_only=True)

	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'profile']
		read_only_fields = ['id']