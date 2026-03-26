from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    paginate_by = 10
    ordering = '-created'
    # queryset = Blog.objects.all().order_by('-created')
    def get_queryset(self):
        queryset = super(BlogListView, self).get_queryset()
        q= self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) |Q(content__icontains=q))
        return queryset

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields=['category','title','content']
    # success_url = reverse_lazy('cb_detail')

    def form_valid(self,form):
        self.object= form.save(commit=False)
        self.object.author= self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse_lazy('blog:detail',kwargs={'pk':self.object.pk})

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields=['category','title','content']
    #
    # # 다른 방법 모델에 정의한 get_absolute_url 사용
    # def get_queryset(self):
    #     queryset= super().get_queryset()
    #     return queryset.filter(author=self.request.user)

    def get_object(self, queryset=None):
        self.object= super().get_object(queryset)
        if self.request.user.is_superuser:
            return self.object

        elif self.object.author != self.request.user:
            raise Http404()
        else:
            return self.object

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset= queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse_lazy('blog:list')