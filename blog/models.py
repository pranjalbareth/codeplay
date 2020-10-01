from django.db import models
from datetime import date
from django.conf import settings

# Create your models here.
class Blog(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	content = models.TextField()
	short_desc = models.CharField(max_length=300, default="")
	poster = models.ImageField(default="") 
	created = models.CharField(max_length=12, default="Sep 09, 2020")
	tag = models.CharField(max_length=30, default="General")
	read_time = models.CharField(max_length=11, default="7 MIN READ")
	slug = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class Application(models.Model):
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=40)
	email = models.CharField(max_length=60)
	desc = models.TextField()
	phone = models.CharField(max_length=10, default="")
	position = models.CharField(max_length=20, default="NOT SPECIFIED")

	def __str__(self):
		return self.name

#auto_now_add=True