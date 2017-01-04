"""PhotoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^me', views.me, name='me'),
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/category/(?P<id>\d+)?$', views.categories, name="categories"),
    url(r'^post/search/$', views.search, name='search'),
    url(r'^post/', views.post_list, name='post_list'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': 'base'}, name='logout'),
    # url(r'^gallery/', include("gallery.urls")),

]
