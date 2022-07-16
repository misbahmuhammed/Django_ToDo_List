from django.shortcuts import render,redirect
from .models import Task
from . forms import TaskForm , UpdateTaskForm
def index(request):
    todos = Task.objects.all()
    count_todos = todos.count()

    completed_todo= Task.objects.filter(complete=True)
    count_completed_todos = completed_todo.count




    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    context = {
        'todos':todos,
        'form': form,
        'count_todos':count_todos,
        'count_completed_todos':count_completed_todos,


            }

    return render(request,'index.html',context)


def update(request,pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':

        form = UpdateTaskForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTaskForm(instance=todo)
    context ={
           'form':form
    }
    return render(request,'update.html',context)

def delete(request,pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':

        todo.delete()
        return redirect('/')
    return render(request,'delete.html')