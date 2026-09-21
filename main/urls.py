from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("achievement/", show_achievement, name="show_achievement"), 
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("experience/add/", create_experience, name="create_experience"),
    path("achievement/add/", create_achievement, name="create_achievement"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("api/achievement/", get_achievement_json, name="get_achievement_json"),
    path("api/experience/", get_experience_json, name="get_experience_json"),    
    path("projects/<uuid:project_id>/delete/",delete_project, name="delete_project"),
    path("experience/<uuid:experience_id>/delete/",delete_experience, name="delete_experience"),
    path("achievement/<uuid:achievement_id>/delete/",delete_achievement, name="delete_achievement"),
]