from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.template import RequestContext
from review.forms import ProjectForm,ProfileForm,BioForm
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


@login_required(login_url='/accounts/register')
def home(request):
	projects = Project.objects.all().order_by('-published').values()
	title = 'Home'
	return render(request, 'projects/index.html', {"projects": projects},{"title":title})

def profile(request,user_id):
	projects = Project.objects.filter(creator_id=user_id)
	profile = Profile.objects.filter(creator_id=user_id).last()
	current_user = request.user

	if request.method == 'POST':
		pform = ProfileForm(request.POST, request.FILES)
		if pform.is_valid():
			print('valid!')
			p_pic = pform.cleaned_data['p_pic']
			bio = pform.cleaned_data['bio']
			creator = pform.cleaned_data['creator']
			profile = Profile(p_pic=p_pic,bio=bio,creator=creator)
			profile.creator = current_user
			profile.save()
		return redirect('profile', user_id)
	else:
		pform = ProfileForm()

	title = 'Profile'

	return render(request, 'user/profile.html', {"projects": projects, "pform": pform, "profile": profile, "title": title})

def bio(request,user_id):
	current_user = request.user
	if request.method == 'POST':
		bioform = BioForm(request.POST)
		if bioform.is_valid():
			print('valid!')
			bio = bioform.cleaned_data['bio']
			bprofile = Profile(bio=bio)
			bprofile.creator = current_user
			bprofile.save()
		return redirect('profile', user_id)
	else:
		bioform = BioForm()

	title = 'Add/Update Bio'

	return render(request, 'user/bio.html', {"bioform": bioform,"title":title})
