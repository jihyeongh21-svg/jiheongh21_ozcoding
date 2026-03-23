from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login
from django.urls import reverse


# Create your views here.
def signup(request):
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    # username 중복 체크
    # 패스워드 규칙 준수 확인


    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)
    """
       아래와  같은 기능 POST 아닐 경우 None 
    """
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/accounts/login/')
    # else:
    #     form = UserCreationForm()

    context = {'form':form}

    return render(request,'registration/signup.html',context)


def login(request):
    form = AuthenticationForm(request,request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())

        next = request.GET.get('next')
        if next:
            return redirect(next)

        return redirect(reverse('blog_list'))
    context = {'form':form}
    return render(request,'registration/login.html',context)
