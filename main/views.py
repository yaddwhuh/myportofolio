from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience
from main.models import Achievement
from main.forms import ProjectForm

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

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Muhammad Fayadh Azzahran",
        "form": form,
    }
    return render(request, "projects_form.html", context)