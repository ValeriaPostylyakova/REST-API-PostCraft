from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	first_name = models.CharField(max_length=150, blank=True)
	last_name = models.CharField(max_length=150, blank=True)
	bio = models.TextField(max_length=700, blank=True)
	avatar = models.URLField(blank=True)

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

	def __str__(self):
		return self.user.email

