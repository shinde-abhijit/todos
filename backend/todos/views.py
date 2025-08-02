from django.shortcuts import render, redirect, get_object_or_404
from todos.models import Todo
from todos.forms import TodoForm
from django.db.models import Q
from datetime import datetime

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user 
            todo.created_by = request.user 
            todo.save()
            return redirect('todo_details', todo.pk)
    else:
        form = TodoForm()
    context ={
        'form': form,
    }
    return render(request, 'todos/add.html', context)



def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    context ={
        'todos': todos
    }
    return render(request, 'todos/list.html', context)



def todo_details(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        'todo':todo,
    }
    return render(request, 'todos/details.html', context)



def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)  
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = todo.user
            todo.updated_by = request.user
            todo.save()
            return redirect('todo_details', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todos/update.html', {'form': form, 'todo': todo})



def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')

    context = {
        'todo': todo,        
    }
    return render(request, 'todos/delete.html', context)



def pending_todo_list(request):
    pending = Todo.objects.filter(user=request.user, status='Pending')
    context ={
        'pending': pending
    }
    return render(request, 'todos/pending.html', context)



def failed_todo_list(request):
    failed = Todo.objects.filter(user=request.user, status='Failed')
    context ={
        'failed': failed
    }
    return render(request, 'todos/failed.html', context)



def completed_todo_list(request):
    completed = Todo.objects.filter(user=request.user, status='Completed')
    context ={
        'completed': completed
    }
    return render(request, 'todos/completed.html', context)



def search_todos(request):
    query = request.GET.get('q', '').strip()
    todo_search = []

    if query:
        todo_search = Todo.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            user=request.user
        )
    
    context = {
        'todo_search': todo_search,
        'query': query,
    }
    return render(request, 'todos/search.html', context)

