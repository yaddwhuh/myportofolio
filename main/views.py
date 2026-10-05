from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
import datetime

from main.models import *
from main.forms import *

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Muhammad Fayadh Azzahran",
        "npm": "2506586961",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student who is also, unfortunately, a furry. "
            "Interests include rhythm games, art, and vocal synthesizers."
        ),
        "last_login": last_login
    }
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser or request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
        
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Muhammad Fayadh Azzharan",
        "form": form,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")    
def create_experience(request):
    if not request.user.is_superuser or request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
        
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

@login_required(login_url="/login/")
def create_achievement(request):
    if not request.user.is_superuser or request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
        
    form = AchievementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Penghargaan baru berhasil ditambahkan!")
        return redirect("main:show_achievement")

    context = {
        "name": "Muhammad Fayadh Azzharan",
        "form": form,
    }
    return render(request, "achievement_form.html", context)
    
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
    
    return JsonResponse(data, safe=False)


def get_achievement_json(request):
    title_query = request.GET.get("title", "").strip()
    achievements = Achievement.objects.prefetch_related('starred_by').all()

    if title_query:
        achievements = achievements.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for achievement in achievements:
        starred_users = achievement.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(achievement.id),
            "fields": {
                "title": achievement.title,
                "description": achievement.description,
                "category": achievement.category,
                "thumbnail": achievement.thumbnail,
                "year": achievement.year,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "thumbnail": experience.thumbnail,
                "started_at": experience.started_at,
                "ended_at": experience.ended_at,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)
    
def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Muhammad Fayadh Azzahran",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "projects.html", context)

def show_achievement(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Muhammad Fayadh Azzahran",
        "title_query": title_query,
        "form": AchievementForm(),
    }
    return render(request, "achievement.html", context)

def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Muhammad Fayadh Azzahran",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")    
def delete_project(request, project_id):
    if not request.user.is_superuser or request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
        
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")    
def delete_achievement(request, achievement_id):
    if not request.user.is_superuser or request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
        
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        achievement.delete()
        messages.success(request, "Penghargaan berhasil dihapus!")
        return redirect("main:show_achievement")

    return redirect("main:show_achievement")
    
@login_required(login_url="/login/")    
def delete_experience(request, experience_id):
    if not request.user.is_superuser or request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
        
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")    
def edit_project(request, project_id):
    if not request.user.is_superuser or request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
        
    project = get_object_or_404(Project, pk=project_id) 
    form = ProjectForm(request.POST, instance=project)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diupdate!")
        return redirect("main:show_projects")

    context = {
        "name": "Muhammad Fayadh Azzharan",
        "form": ProjectForm(instance=project),
        "project": project,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")    
def edit_experience(request, experience_id):
    if not request.user.is_superuser or request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
        
    experience = get_object_or_404(Experience, pk=experience_id) 
    form = ExperienceForm(request.POST, instance=experience)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diupdate!")
        return redirect("main:show_experience")

    context = {
        "name": "Muhammad Fayadh Azzharan",
        "form": ExperienceForm(instance=experience),
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")    
def edit_achievement(request, achievement_id):
    if not request.user.is_superuser or request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
        
    achievement = get_object_or_404(Achievement, pk=achievement_id) 
    form = AchievementForm(request.POST, instance=achievement)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Penghargaan berhasil diupdate!")
        return redirect("main:show_achievement")

    context = {
        "name": "Muhammad Fayadh Azzharan",
        "form": AchievementForm(instance=achievement),
        "achievement": achievement,
    }
    return render(request, "achievement_form.html", context)
    
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Muhammad Fayadh Azzahran",
        "form": form,
    }
    return render(request, "register.html", context)
    
def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Muhammad Fayadh Azzahran",
        "form": form,
    }
    return render(request, "login.html", context)
    
def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie("last_login")
    return response
    
@login_required(login_url="/login/")
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def toggle_star_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        if request.user in achievement.starred_by.all():
            achievement.starred_by.remove(request.user)
        else:
            achievement.starred_by.add(request.user)

    return redirect("main:show_achievement")

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")
    
def is_user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
    
@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
    
@require_POST
def create_achievement_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan penghargaan."},
            status=403,
        )

    form = AchievementForm(request.POST)
    if form.is_valid():
        achievement = form.save()
        return JsonResponse(
            {"message": "Penghargaan berhasil ditambahkan.", "pk": str(achievement.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
    
@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pengalaman."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Pengalaman berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)