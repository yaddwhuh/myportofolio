from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Achievement, Project
from main.forms import ProjectForm, ExperienceForm

def show_main(request):
    context = {
        "name": "Muhammad Fayadh Azzahran",
        "npm": "2506586961",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student who is also, unfortunately, a furry. "
            "Interests include rhythm games, art, and vocal synthesizers."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Muhammad Fayadh Azzahran",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
    
def show_achievement(request):
    context = {
        "name": "Muhammad Fayadh Azzahran",
        "achievement_list": Achievement.objects.all(),
    }
    return render(request, "achievement.html", context)

def show_project(request):
    context = {
        "name": "Muhammad Fayadh Azzahran",
        "project_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Muhammad Fayadh Azzharan",
        "form": form,
    }
    return render(request, "projects_form.html", context)
    
def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Muhammad Fayadh Azzharan",
        "form": form,
    }
    return render(request, "experience_form.html", context)
    
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")
