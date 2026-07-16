from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tarefas = Task.objects.filter(usuario=request.user)
    return render(request, 'tasks/task_list.html', {'tarefas': tarefas})

def task_create(request):

    if request.method == "POST":

        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        Task.objects.create(
            usuario=request.user,
            titulo=titulo,
            descricao=descricao
        )

        return redirect('task_list')

    return render(request, 'tasks/task_create.html')

def task_edit(request, id):

    tarefa = get_object_or_404(Task, id=id)

    if request.method == "POST":

        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.concluido = request.POST.get('concluido') == 'True'

        tarefa.save()

        return redirect('task_list')


    return render(request, 'tasks/task_edit.html', {'tarefa': tarefa})