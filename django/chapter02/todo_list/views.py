from django.http import HttpResponse
from django.shortcuts import render

from todo_list.models import TodoList


# Create your views here.

def index(request):
    return HttpResponse('<h1>todo_list</h1>')

def todo_list(request):
    todo_list = TodoList.objects.all()
    context = {'todo_list': todo_list}

    return render(request, 'todo_list.html', context)

def todo_info(request, pk):
    todo = TodoList.objects.get(pk=pk)
    context = {'todo':todo}
    return render(request,'todo_info.html',context)