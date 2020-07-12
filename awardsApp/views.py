import datetime as dt
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import AddProjectForm, RateProjectForm, CreateProfileForm
from .email import send_signup_email
from .models import Profile, Project
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404

def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = CreateProfileForm()
    return render(request, 'user/create_profile.html', {"form": form})

def email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_signup_email(name, email)
    return redirect(create_profile)
    
@login_required(login_url='/accounts/login/')
def home(request):
    title= "aWWWards"
    date = dt.date.today()
    projects = Project.display_all_projects()
    projects_scores = projects.order_by('-average_score')
    highest_score = projects_scores[0]
    return render(request, "home.html", {"date": date, "title": title, "projects": projects, "highest":highest_score})

def profile(request):
    return render(request, "user/profile.html")

def project(request, project_id):
    form = RateProjectForm()
    return render(request, 'project/project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_project(request):
    if request.method == "POST":
        form = AddProjectForm(request.POST, request.FILES)
        current_user = request.user
        try:
            profile = Profile.objects.get(user = current_user)
        except Profile.DoesNotExist:
            raise Http404()
        if form.is_valid():
            project = form.save(commit= False)
            project.profile = profile
            project.save()
        return redirect("home")
    else:
        form = AddProjectForm()
    return render(request, 'project/add_project.html', {"form": form})

def rate_project(request,id):
    project = Project.objects.get(pk = id)
    if request.method == "POST":
        form = RateProjectForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']

            project.design_score = project.design_score + design
            project.usability_score = project.usability_score + usability
            project.content_score = project.content_score + content

            project.average_design = project.design_score/project.voters_count()
            project.average_usability = project.usability_score/project.voters_count()
            project.average_content = project.content_score/project.voters_count()

            project.average_score = (project.average_design + project.average_usability + project.average_content)/3

            project.save()
            return HttpResponseRedirect(reverse('project'))

    else:
        form = RateProjectForm()
    return render(request, 'project/project.html', {"form": form})

def search_project(request):
    if "project" in request.GET and request.GET["project"]:
        searched_project = request.GET.get("project")
        try:
            projects = Project.search_project(searched_project)
            message =f"{searched_project}"
            if len(projects) == 1:
                project = projects[0]
                form = RateProjectForm()
                return render(request, 'project/project.html', {"form": form, "project": project})
            return render(request, 'project/search.html', {"projects": projects,"message": message})
        except ObjectDoesNotExist:
            projects = Project.display_all_projects()
            if len(projects)> 1:
                suggestions = projects[:4]
                message= f"Found NO projects titled {searched_project}"
                return render(request, 'project/search.html', {"suggestions":suggestions,"message": message})
    else:
        message = "You haven't searched for any term"
        return render(request,'project/search.html', {"message": message})