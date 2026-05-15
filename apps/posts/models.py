from django.db import models
from django.contrib.auth.models import User
from ..tags.models import Tag
from ..categories.models import Category

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	image_url = models.URLField(blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')

	def __str__(self):
		return self.title
