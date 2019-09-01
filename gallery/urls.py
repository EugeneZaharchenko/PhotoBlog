"""PhotoBlog URL Configuration
"""
from django.conf.urls import url
from .views import gallery, upload\
    # , country

urlpatterns = [
    url(r'^$', gallery, name="gallery"),
    url(r'^upload/$', upload, name="upload"),
    # url(r'country/(?P<id>\d+)/$', country, name="country"),
    # url(r'^certain_photo/$', certain_photo, name="certain_photo"),
]
