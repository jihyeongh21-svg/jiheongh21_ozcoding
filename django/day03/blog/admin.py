from django.contrib import admin

from blog import models

# Register your models here.
@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    ...