from django import forms
from .models import Profile,Project,Contact


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['p_pic','bio']
		exclude = ['creator']

class BioForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ['p_pic','creator']


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['landing_pic','short_description','long_description','support_pic_a','support_pic_b']

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['first_name','last_name','email','phone','address']
		exclude = ['creator']

