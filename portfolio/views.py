from django.shortcuts import render
from .models import Project, Media
def home(request):
    context = {
        'project': Project.objects.all()
    }
    return render(request, 'index.html', context=context)

def details(request, id):
    project = Project.objects.get(id=id)
    media = Media.objects.filter(project_id=id)
    context = {
        'project': project,
        'media': media
    }
    return render(request, 'portfolio-details.html', context=context)
# Create your views here.
