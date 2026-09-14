from django.shortcuts import render

from main.models import Experience
from main.models import Achievement

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