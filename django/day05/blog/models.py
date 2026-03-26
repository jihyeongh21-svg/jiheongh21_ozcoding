from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()
# Create your models here.

"""
블로그 모델 
1. 제목
2. 본문
3. 작성자
4. 작성일자
5. 수정일자
6. 카테고리
"""
class Blog(models.Model):
    CATEGORY_CHOICES = (
        ('free','자유'),
        ('travel','여행'),
        ('study','공부'),
        ('food','음식')
    )

    category = models.CharField('카테고리',max_length = 20,choices = CATEGORY_CHOICES,default = 'free')
    # 작성자 추후 추가
    title = models.CharField('제목',max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField('생성일자',auto_now_add=True)
    updated = models.DateTimeField('수정일자',auto_now=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'




