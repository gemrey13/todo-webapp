from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=200)
	status = models.CharField(max_length=20, default='todo')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'Title: {self.title}'

