from django.contrib import admin
from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'text', 'created_date', 'published_date', 'category')
    list_filter = ('title', 'author', 'created_date', 'published_date', 'category', 'img')
    search_fields = ('title', 'author', 'text')
    ordering = ('created_date', 'category')
    date_hierarchy = 'published_date'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'gender', 'created_date', 'mail')
    list_filter = ('post', 'author', 'gender', 'created_date', 'mail', 'approved_comment')
    search_fields = ('post', 'author', 'text')
    ordering = ('post', 'author', 'created_date')
    date_hierarchy = 'created_date'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    list_filter = 'name',
    search_fields = 'name',
    ordering = 'name',
