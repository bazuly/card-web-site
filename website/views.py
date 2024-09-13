from django.shortcuts import render
from .models import *


def project_main_page(request):
    projects = Project.objects.all()
    context_project = {'projects': projects}
    return render(request, 'project_main_page.html', context_project)


def resume_info(request):
    resume = Resume.objects.all()
    context_resume = {'resume': resume}
    return render(request, 'resume_info_main_page.html', context_resume)


def contact_info(request):
    contact = ContactInfo.objects.all()
    context_contact = {'contact': contact}
    return render(request, 'contact_info_main_page.html', context_contact)

