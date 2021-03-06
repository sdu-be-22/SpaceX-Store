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
class Order(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=128)
        postcode = models.CharField(max_length=8)
        address = models.CharField(max_length=256)
class Cart(models.Model):
        book = models.ForeignKey(Book, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        done = models.BooleanField(default=False)
        ordering = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
	
	class Comment(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=1024)
