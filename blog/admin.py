from django.contrib import admin
from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'author', 'status']
    search_fields = ['title', 'body']
    prepopulated_fields = { 'slug': ('title', )}
    # raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    list_filter = ['status', 'publish']

admin.site.register(Post, PostAdmin) # Register


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    search_fields =  ['name', 'email', 'body']
    list_filter = ['active', 'created', 'updated']

admin.site.register(Comment, CommentAdmin)