from todo_list.models import TodoList
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title','description','start_date','end_date']

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title','description','start_date','end_date','is_completed']
