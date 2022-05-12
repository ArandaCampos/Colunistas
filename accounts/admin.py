from atexit import register
from django.contrib import admin
from django.contrib.admin import register
from accounts.models import UserModels, PostsModels

# Register your models here.
admin.site.register(UserModels)
# class adminUserModels(admin.ModelAdmin):
#     list_display = ('name', 'posts')

@admin.register(PostsModels)
class adminPostsModels(admin.ModelAdmin):
    list_display = ('author', 'title', 'text')
    prepopulated_fields = {'slug': ('title',)}