from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.template import RequestContext
from review.forms import ProjectForm,ProfileForm
from review.models import Profile,Project

# Create your views here.
@login_required(login_url='/accounts/login/')
def new_project(request):
	current_user = request.user
	if request.method == 'POST':
		form = ProjectForm(request.POST,request.FILES)
		if form.is_valid():
			print('valid!')
			landing_pic = form.cleaned_data['landing_pic']
			description = form.cleaned_data['description']
			support_pic_a = form.cleaned_data['support_pic_a']
			caption_a = form.cleaned_data['caption_a']
			support_pic_b = form.cleaned_data['support_pic_b']
			caption_b = form.cleaned_data['caption_b']

			usr_project = Project(landing_pic=landing_pic,description=description,support_pic_a=support_pic_a,caption_a=caption_a,support_pic_b=support_pic_b,caption_b=caption_b)
			usr_project.creator = current_user
			usr_project.save()
		return redirect('profile')
	else:
		form = ProjectForm()

	title = 'Add Project'

	return render(request,'user/upload.html',{"form":form},{"title":title})
