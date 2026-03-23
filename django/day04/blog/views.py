from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import BlogForm
from blog.models import Blog
from django.urls import reverse

# Create your views here.

from django.core.paginator import Paginator

from django.views.decorators.http import require_http_methods

## blog/views.py

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created') # 수정

    q= request.GET.get('q')
    # print(q)
    if q:
        blogs = blogs.filter(
            Q(title__icontains=q)|
            Q(content__icontains=q)
        )
        # blogs = blogs.filter(title__icontains=q)
    paginator = Paginator(blogs, 10)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
    }

    return render(request, 'blog_list.html', context)

def blog_detail(request, pk):
    blog= get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request,'blog_detail.html',context)

@login_required()
def blog_create(request):
    # if not request.user.is_authenticated:
    #     return redirect(reverse('login'))
    #위의 코드와 같은 기능 @login_required()  -> setting에 등록한 LOGIN URL 로 이동

    form = BlogForm(request.POST or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        return redirect("blog_detail",blog.pk)
    context = {'form': form}
    return render(request,'blog_create.html',context)
## blog/views.py


@login_required()
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)

    form = BlogForm(request.POST or None, instance=blog) # instance로 기초데이터 세팅
    if form.is_valid():
        blog = form.save()
        return redirect(reverse('blog_detail', kwargs={'pk': blog.pk}))

    context = {'blog': blog,
               'form' : form,
               }

    return render(request, 'blog_update.html', context)

@login_required()
@require_http_methods(['POST']) # 특정 메소드 지정
def blog_delete(request, pk):
    # if request.method != 'POST':
    #     raise Http404()
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    blog.delete()
    return redirect(reverse('blog_list'))

