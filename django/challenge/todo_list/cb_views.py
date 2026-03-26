
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from todo_list.models import TodoList


class TodoListListView(LoginRequiredMixin,ListView):
    model = TodoList
    template_name = 'todo_list.html'
    ordering = 'start_date'
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()
        if  not self.request.user.is_superuser:
            queryset = super().get_queryset().filter(user=self.request.user)
        q=self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q)|
                Q(description__icontains=q)
            )
        return queryset


class TodoListDetailView(LoginRequiredMixin,DetailView):
    model = TodoList
    template_name = 'todo_info.html'




class TodoListCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    template_name = 'todo_create.html'
    fields = ['title','description','start_date','end_date']

    def form_valid(self, form):
        # self.object = form.save(commit=False)
        # self.object.user = self.request.user
        # self.object.save()
        # return HttpResponseRedirect(self.get_success_url())

        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_success_url(self):
        return reverse_lazy('todo:info',kwargs={'pk':self.object.pk})


class TodoListUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoList
    template_name = 'todo_update.html'
    fields = ['title','description','start_date','end_date','is_completed']

    def get_queryset(self):
        queryset = super().get_queryset()
        if  not self.request.user.is_superuser:
            return queryset.filter(user=self.request.user)
        return queryset

class TodoListDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoList
    def get_queryset(self):
       queryset= super().get_queryset()
       if not self.request.user.is_superuser:
           return queryset.filter(user=self.request.user)
       return queryset

    def get_success_url(self):
        return reverse_lazy('todo:list')
