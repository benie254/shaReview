from django.db import models
import datetime as dt
from location_field.models.plain import PlainLocationField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.


class Project(models.Model):
	creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
	landing_pic = CloudinaryField('image')
	short_description = models.CharField(max_length=30)
	long_description = models.CharField(max_length=60)
	support_pic_a = CloudinaryField('image')
	support_pic_b = CloudinaryField('image')
	published = models.DateTimeField(auto_now_add=True)

	@classmethod
	def search_by_term(cls, search_term):
		projects = cls.objects.filter(long_description__icontains=search_term)
		return projects

class Profile(models.Model):
	creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
	username = models.CharField(max_length=60)
	bio = models.CharField(max_length=60, null=True)
	p_pic = CloudinaryField('image', null=True)
	created = models.DateTimeField(auto_now_add=True)


class Voter(models.Model):
	username = models.CharField(max_length=60)
	display_name = models.CharField(max_length=60)
	bio = models.CharField(max_length=60, null=True)
	p_pic = CloudinaryField('image', null=True)
	created = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
	creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	email = models.EmailField()
	phone = models.PositiveIntegerField(default=254)
	address = models.CharField(max_length=60)
