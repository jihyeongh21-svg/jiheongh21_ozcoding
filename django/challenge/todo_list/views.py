from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render

from todo_list.models import TodoList


# Create your views here.

def index(request):
    return HttpResponse('<h1>todo_list</h1>')

@ login_required
def todo_list(request):
    todo_list = TodoList.objects.all()
    context = {'todo_list': todo_list}

    return render(request, 'todo_list.html', context)
@ login_required
def todo_info(request, pk):
    todo = TodoList.objects.get(pk=pk)
    if not todo:
        raise Http404
    context = {'todo':todo}
    return render(request,'todo_info.html',context)