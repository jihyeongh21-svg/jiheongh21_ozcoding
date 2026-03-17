"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse, Http404
from django.urls import path
from django.shortcuts import render

game_list =[
    {"tittle": "리그오브레전드","company":"라이엇"},
    {"tittle": "발로란트","company":"라이엇"},
    {"tittle": "리니지 클래식","company":"nc소프트"},
    {"tittle": "배틀 그라운드","company":"pubg"}
]
book_list=[
    {"title":"소년이 온다","author":"한강"},
    {"title":"모순","author":"양귀자"},
    {"title":"결국 국민이 합니다","author":"이재명"},
    {"title":"혼모노","author":"성해나"}
]

# 책 리스트
def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")
def books(request):

  return render(request,template_name='books.html',context={'book_list':book_list})

def book(request,i):
    book = book_list[i]
    return render(request,template_name='book.html',context={'book':book})

def books_list(request):
    return render(request,template_name='books_list.html',context={'range': range(0,10)})

def book_detail(request,num):
    return render(request,template_name='book_detail.html',context={'num':num})
def langauge(request,rang):
    return HttpResponse(f"<h1>{rang} 언어 페이지 입니다</h1>")

def python(request):
    return HttpResponse(f"<h1>python</h1>")

# 게임 순위
def games(request):
    # game_titles = [
    #      f"<a href='/game/{index}/'>{game['tittle']}</a>"
    #      for index, game in enumerate(game_list)
    # ]
    #
    # response_text = '<br>'.join(game_titles)
    # return HttpResponse(response_text)
    return render(request,template_name='games.html',context={'game_list':game_list})
def game_detail(request,index):
    if index >= len(game_list)-1:
        raise Http404()
    game = game_list[index]
    context = {'game':game}
    return render(request,template_name='game.html',context=context)

# 구구단
def dan(request):
    return render(request,template_name='dan.html',context={'range': range(2,10)})
def gugudan(request,dan):
    context = {'dan':dan,
               'result':[dan*i for i in range(1,10)],}
    return render(request,template_name='gugudan.html',context=context)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('books/', books),

    path('book/<int:i>/',book),
    path('langauge/python/',python),
    path('langauge/<str:rang>/', langauge),

    path('games/',games),

    path('game/<int:index>/',game_detail),

    path('books_list/',books_list),

    path('book_detail/<int:num>/',book_detail),

    path('dan/',dan),

    path('gugudan/<int:dan>/',gugudan),
]
