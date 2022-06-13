from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('creator','landing_pic','short_description','long_description')