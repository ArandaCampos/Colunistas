from django.contrib import admin
from accounts.models import UserModels, PostsModels

# Register your models here.

admin.site.register(UserModels)

@admin.register(PostsModels)
class adminPostsModels(admin.ModelAdmin):
    list_display = ('author', 'title', 'text')
    prepopulated_fields = {'slug': ('title',)}