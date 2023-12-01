from django.shortcuts import render
from .models import Home, About, Profile, Services, CV
from portfolio.models import Project

# Create your views here.

def home(request):

    # Home
    home_page = Home.objects.latest('Updated')
    SM_info = home_page.socialmedia_set.all()

    # CV Instance

    cv_instance = CV.objects.get()

    # About
    about_page = About.objects.latest('Updated')
    profiles = Profile.objects.filter(about_page = about_page)

    # Services
    service_page = Services.objects.all()

    # Projects
    projects = Project.objects.all()

    context = {
        "home_page": home_page,
        "SM_info": SM_info,
        "cv_instance": cv_instance,
        "about_page": about_page,
        "profiles": profiles,
        "service_page": service_page,
        "projects": projects
    }
    return render(request, 'pages/index.html', context)
