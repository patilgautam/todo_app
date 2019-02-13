from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from todoapp.models import Todo
from todoapp.forms import TodoForm

#List all ToDo List
def index(request):
    todo_list=Todo.objects.all()
    # print(todo_list)
    form=TodoForm()
    context={'todo_list':todo_list,'form':form}
    return render(request,'index.html',context)

#Add ToDo items
@require_POST
def addTodo(request):
    form=TodoForm(request.POST)
    if form.is_valid():
        new_todo=Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

#Mark ToDO item as completed
def completeTodo(request,todo_id):
    todo=Todo.objects.get(pk=todo_id)
    todo.complete=True
    todo.save()
    # pass
    return redirect('index')

#Delete all completed ToDO items
def deleteCompletedTodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')
    # pass

#Delete all ToDO items
def deleteAllTodo(request):
    Todo.objects.all().delete()
    return redirect('index')