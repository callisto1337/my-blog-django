from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 100)
	preview_post = models.TextField(max_length = 200, default='')
	text = models.TextField()
	date_created = models.DateTimeField()

	def __str__(self):
		return self.title