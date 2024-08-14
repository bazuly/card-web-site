from django import forms
from .models import Resume, Project, ContactInfo


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'description', 'file']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'file']


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name', 'email', 't_me']
