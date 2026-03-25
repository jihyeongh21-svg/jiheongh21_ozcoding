from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from todo_list.models import TodoList
from todo_list.form import TodoForm, TodoUpdateForm


# Create your views here.

def index(request):
    return HttpResponse('<h1>todo_list</h1>')

@ login_required
def todo_list(request):
    todo_list = TodoList.objects.filter(user=request.user).order_by('start_date')

    q= request.GET.get('q')
    if q:
        todo_list = todo_list.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q)
        )
    paginator = Paginator(todo_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj}

    return render(request, 'todo_list.html', context)
@ login_required
def todo_info(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    context = {'todo':todo}
    return render(request,'todo_info.html',context)

@login_required
def create_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect("todo_list")
    context = {'form':form}
    return render(request,'todo_create.html',context)


@login_required
def update_todo(request, pk):
    todo = get_object_or_404(TodoList, pk=pk, user=request.user)
    form = TodoUpdateForm(request.POST or None,instance=todo)
    if form.is_valid():
        todo = form.save()
        return redirect('todo_info',pk=todo.pk)
    context = {
        'todo':todo,
        'form':form
            }
    return render(request,'todo_update.html',context)


@require_http_methods(['POST'])
@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    todo.delete()
    return redirect('todo_list')



