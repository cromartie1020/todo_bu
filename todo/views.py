from django.shortcuts import render,get_object_or_404, redirect
from .models import Todo_List
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'todo/index.html')

def about(request):
    pass

def todo_list(request):
    todos = Todo_List.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/todo_list.html', context)

def todo_detail(request, pk):
    todo = get_object_or_404(Todo_List, pk=pk)
    context = {'todo': todo}
    return render(request, 'todo/todo_detail.html', context)

@login_required
def todo_create(request):
    if request.method == 'POST':
        new_todo = request.POST.get('new_todo')
        author = request.user
        Todo_List.objects.create(new_todo=new_todo, author=author)
        return redirect('todo_list')
    return render(request, 'todo/todo_create.html')

def todo_update(request, pk):
    todo = get_object_or_404(Todo_List, pk=pk)
    if request.method == 'POST':
        todo.new_todo = request.POST.get('new_todo')
        todo.save()
        return redirect('todo_detail', pk=todo.pk)
    context = {'todo': todo}
    return render(request, 'todo/todo_update.html', context)

def todo_delete(request, pk):
    todo = get_object_or_404(Todo_List, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    context = {'todo': todo}
    return render(request, 'todo/todo_delete.html', context)    