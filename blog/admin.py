from django.contrib import admin
from blog.models import Category, Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_editable = ['title']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']


admin.site.register(Category)
admin.site.register(Post, PostModelAdmin)