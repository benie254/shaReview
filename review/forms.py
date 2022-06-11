from django import forms
from .models import Profile,Project


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['p_pic','bio','creator']


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['landing_pic','description','support_pic_a','caption_a','support_pic_b','caption_b']

