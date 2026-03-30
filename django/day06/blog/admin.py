from django.contrib import admin

from blog import models

# Register your models here.

admin.site.register(models.Comment)
class CommentInline(admin.TabularInline):
    model = models.Comment
    fields = ['content','author']
    extra = 1


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]