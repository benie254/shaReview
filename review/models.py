from django.db import models
import datetime as dt
from location_field.models.plain import PlainLocationField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    p_pic = CloudinaryField('image', null=True)
    bio = models.CharField(max_length=60,null=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

class Project(models.Model):
	landing_pic = CloudinaryField('image')
	description = HTMLField()
	support_pic_a = CloudinaryField('image')
	caption_a = HTMLField()
	support_pic_b = CloudinaryField('image')
	caption_b = HTMLField()

