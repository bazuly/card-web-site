from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project_main_page, name='project_main_page'),
    path('resume/', views.resume_info, name='resume_info'),
    path('contact/', views.contact_info, name='contact_info'),
]
