from django.db import models
from django.contrib.auth.models import User
from ..posts.models import Post

class Comment(models.Model):
	content = models.TextField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	

