from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.all_nika, name='all_nika'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('<int:nika_id>/', views.project_details, name='project_details'),
    path('interests/', views.cultivated_pursuits, name='interest'),
    path('<int:nika_id>/', views.interests_details, name='interests_details'),
    path('contact_me/', views.contact_me, name='contact_me'),
    path('contact_submit/', views.contact_submit, name='contact_submit'),
]
