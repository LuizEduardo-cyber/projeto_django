from django.shortcuts import render

def task_list(request):
    return render(request, 'tasks/task_list.html')

def task_create(request):
    return render(request, 'tasks/task_create.html')

def task_edit(request):
    return render(request, 'tasks/task_edit.html')
# Create your views here.
