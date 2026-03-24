from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

class TodoList(models.Model):
    title = models.CharField('할일',max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    class Meta:
        db_table = 'todo_list'
        verbose_name = '해야할 일'
        verbose_name_plural = '해야할 일 목록'