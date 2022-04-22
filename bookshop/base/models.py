from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Genre(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name 

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=128)
	image = models.ImageField(upload_to='images/', blank=True)

	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

	price = models.IntegerField(default=0)
	about = RichTextField()

	def __str__(self):
		return self.name
