from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.auth import login, logout

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_list')
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    # url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/category/(?P<id>\d+)/$', views.category, name="category"),
    # url(r'^post/tag/(?P<id>\d+)/$', views.tag, name='tag'),
    # url(r'^post/search/$', views.search, name='search'),
    # url(r'^post/', views.post_list, name='post_list'),
    # url(r'^login/$', login, name='login'),
    # url(r'^logout/$', logout, {'next_page': 'base'}, name='logout'),
    # url(r'^gallery/', include("gallery.urls")),
]
