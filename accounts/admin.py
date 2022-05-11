from atexit import register
from django.contrib import admin
from accounts.models import UserModels, PostsModels

# Register your models here.
@admin.register(UserModels)
class adminUserModels(admin.ModelAdmin):
    list_display = ('name', 'follower', 'posts')

@admin.register(PostsModels)
class adminPostsModels(admin.ModelAdmin):
    list_display = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}