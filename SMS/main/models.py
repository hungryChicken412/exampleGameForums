from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from autoslug import AutoSlugField

import sys
sys.path.append('..')


# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(default='', upload_to='blogThumbs/')
	intro = models.TextField(max_length=200)
	content = models.TextField()
	published = models.DateTimeField(default=datetime.now())

	slug = AutoSlugField(populate_from='title')
	

	def __str__(self):
		return self.title


class Game(models.Model):
	title = models.CharField(max_length=200)
	thumbnail = models.ImageField(default='', upload_to='blogThumbs/')
	description = models.TextField(max_length=200)
	price = models.FloatField()
	buy_url = models.URLField()
	

	def __str__(self):
		return self.title

class Screenshots(models.Model):
	thumbnail = models.ImageField(default='', upload_to='screenshots/')

class LandingPageDetails(models.Model):
	heroImage = models.ImageField(default='', upload_to='screenshots/')
	logo = models.ImageField(default='', upload_to='screenshots/')
	description = models.TextField()

	def __str__(self):
		return "Landing Page Details, Please Keep only one of these objects"
	

