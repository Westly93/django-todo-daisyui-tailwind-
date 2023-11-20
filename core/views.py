from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required
def index(request):
    context={
        "form": TodoForm(),
        "todos": Todo.objects.all()
    }
    return render(request, 'core/index.html', context)
@login_required
@require_http_methods(['POST'])
def add_todo(request):
    form= TodoForm(request.POST)
    if form.is_valid():
        todo= form.save(commit= False)
        todo.user= request.user
        todo.save()
        context={
            'todo': todo
        }
        return render(request, 'core/index.html#todo-partial', context)
    
    
@login_required  
@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo= get_object_or_404(Todo, pk= pk, user= request.user)
    todo.is_completed= True
    todo.save()
    context={
        'todo': todo,
    }
    return render(request, 'core/index.html#todo-partial', context)
@login_required
@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo= get_object_or_404(Todo, pk=pk, user= request.user)
    todo.delete()
    response= HttpResponse(status= 204)
    response['HX-Trigger']= "delete-todo"
    return response