"""PhotoBlog Gallery URL Configuration
"""
from django.urls import path
from blog.views import BaseView
from .views import GalleryView, upload


urlpatterns = [
    path('', GalleryView.as_view(), name="gallery"),
    # url(r'^upload/$', upload, name="upload"),
    # url(r'^certain_photo/$', certain_photo, name="certain_photo"),
]
