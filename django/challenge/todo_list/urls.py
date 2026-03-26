from django.urls import path

from todo_list  import cb_views

app_name = 'todo'

urlpatterns = [
    path('',cb_views.TodoListListView.as_view(),name='list'),
    path('<int:pk>/',cb_views.TodoListDetailView.as_view(),name='info'),
    path('create/',cb_views.TodoListCreateView.as_view(),name='create'),
    path('<int:pk>/update/',cb_views.TodoListUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',cb_views.TodoListDeleteView.as_view(),name='delete'),
 ]