from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'author', 'status']
    search_fields = ['title', 'body']
    prepopulated_fields = { 'slug': ('title', )}
    # raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    list_filter = ['status', 'publish']

admin.site.register(Post, PostAdmin) # Register