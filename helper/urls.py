from django.urls import path

from . import views

urlpatterns = [
    path("project-detail/<int:pk>/", views.project_detail, name="project-detail"),
    path("projects/", views.projects_page, name="projects"),
    path("about/", views.about_page, name="about"),
    path("", views.home_page, name="home"),
]
