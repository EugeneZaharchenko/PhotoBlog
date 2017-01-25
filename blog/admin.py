from django.contrib import admin
from .models import Post, Comment, Category, Tag
from django.db import models


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
