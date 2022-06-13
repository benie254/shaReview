from rest_framework import serializers
from .models import Project,Profile


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('creator_id','landing_pic','short_description','long_description')

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ('creator_id','username','bio','username','p_pic')

