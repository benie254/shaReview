from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.template import RequestContext
from review.forms import ProjectForm,ProfileForm,BioForm,ContactForm
from review.models import Profile,Project,Contact

# Create your views here.
@login_required(login_url='/accounts/login/')
def new_project(request):
	current_user = request.user

	if request.method == 'POST':
		projform = ProjectForm(request.POST, request.FILES)
		if projform.is_valid():
			print('valid!')
			landing_pic = projform.cleaned_data['landing_pic']
			description = projform.cleaned_data['description']
			support_pic_a = projform.cleaned_data['support_pic_a']
			caption_a = projform.cleaned_data['caption_a']
			support_pic_b = projform.cleaned_data['support_pic_b']
			caption_b = projform.cleaned_data['caption_b']
			project = Project(landing_pic=landing_pic,description=description,support_pic_a=support_pic_a,caption_a=caption_a,support_pic_b=support_pic_b,caption_b=caption_b)
			project.creator = current_user
			project.save()
		return redirect('home')
	else:
		projform = ProjectForm()

	title = 'Add Project'

	return render(request, 'user/upload.html',{"projform": projform,"title":title})

def search_results(request):

	if 'project' in request.GET and request.GET["project"]:
		search_term = request.GET.get("project")
		searched_projects = Project.search_by_term(search_term)
		message = f"{search_term}"

		return render(request,'projects/search_results.html',{"message":message,"projects":searched_projects})
	else:
		message = "You haven't searched for an image yet"

		return render(request,'projects/search_results.html',{"message":message})



def home(request):
	projects = Project.objects.all()

	title = 'Home'
	return render(request, 'projects/index.html', {"projects": projects,"title": title})

def profile(request,user_id):
	projects = Project.objects.filter(creator_id=user_id)
	profile = Profile.objects.filter(creator_id=user_id).last()
	contact = Contact.objects.filter(pk=user_id).first()
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

	return render(request, 'user/profile.html', {"projects": projects, "pform": pform, "profile": profile, "title": title,"contact":contact})

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


@login_required(login_url='/accounts/login')
def project(request,project_id):
	try:
		project = Project.objects.get(id=project_id)

	except DoesNotExist:
		raise Http404()

	title = 'Project'

	return render(request,'projects/project.html',{"project":project,"title":title})

def contact(request,user_id):
	current_user = request.user
	if request.method == 'POST':
		contform = ContactForm(request.POST)
		if contform.is_valid():
			print('valid!')
			first_name = contform.cleaned_data['first_name']
			last_name = contform.cleaned_data['last_name']
			email = contform.cleaned_data['email']
			phone = contform.cleaned_data['phone']
			address = contform.cleaned_data['address']
			pcontact = Contact(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address)
			pcontact.creator = current_user
			pcontact.save()
		return redirect('profile', user_id)
	else:
		contform = ContactForm()

	title = 'Contact Info'

	return render(request, 'user/contact.html', {"contform": contform,"title":title})
