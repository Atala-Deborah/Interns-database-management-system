
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InternForm
from .models import Intern
from .models import Workshop
from .forms import WorkshopForm
from datetime import date
from .models import Project
from .forms import ProjectForm

def intern_list(request):
    interns = Intern.objects.all()
    return render(request, 'database/registry.html', {'interns': interns})

def add_intern(request):
    if request.method == 'POST':
        form = InternForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('intern_registry')
    else:
        form = InternForm()
    return render(request, 'database/add_intern.html', {'form': form})

def edit_intern(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    if request.method == 'POST':
        form = InternForm(request.POST, instance=intern)
        if form.is_valid():
            form.save()
            return redirect('intern_registry')
    else:
        form = InternForm(instance=intern)
    return render(request, 'database/edit_intern.html', {'form': form})

def intern_registry(request):
    interns = Intern.objects.all()
    return render(request, 'database/registry.html', {'interns': interns})

def dashboard(request):
    return render(request, 'database/dashboard.html')  # Adjust path if needed

def delete_intern(request, id):
    intern = get_object_or_404(Intern, id=id)
    if request.method == "POST":
        intern.delete()
    return redirect('intern_registry')  # adjust to your registry view name


def workshops_view(request):
    ongoing = Workshop.objects.filter(date__gte=date.today())
    return render(request, 'database/workshops.html', {'workshops': ongoing})

def past_workshops_view(request):
    past_workshops = Workshop.objects.filter(date__lt=date.today()).order_by('-date')
    return render(request, 'database/past_workshops.html', {'past_workshops': past_workshops})

def create_workshop_view(request):
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('workshops')
    else:
        form = WorkshopForm()
    return render(request, 'database/create_workshop.html', {'form': form})
def dashboard(request):
    upcoming_workshops = Workshop.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, 'database/dashboard.html', {'workshops': upcoming_workshops})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'database/projects.html', {'projects': projects})


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'database/create_project.html', {'form': form})

