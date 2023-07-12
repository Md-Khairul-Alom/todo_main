
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def addtask(request):
    task=request.POST['task']
    Task.objects.create(task=task).order_by('-updated_at')
    return redirect('home')