from django.shortcuts import render
from constants import NAME, TITLE, ABOUT, TECHNOLOGIES, PROJECTS, GITHUB, LINKEDIN

def portfolio(request):
    profile = {
        'name': NAME,
        'title': TITLE,
        'about': ABOUT,
        'technologies': TECHNOLOGIES,
        'projects': PROJECTS,
    }
    return render(request, 'portfolio.html', {'profile': profile})
