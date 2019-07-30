from django.urls import path, re_path, include
from . import views
from django.contrib.auth import login, logout

urlpatterns = [
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/(?P<pk><int:num>)/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/(?P<pk><int:num>)/remove/', views.post_remove, name='post_remove'),
    path('post/(?P<pk><int:num>)/', views.post_detail, name='post_detail'),
    path('post/category/(?P<id><int:num>)/', views.category, name="category"),
    path('post/tag/(?P<id><int:num>)/', views.tag, name='tag'),
    path('post/search/', views.search, name='search'),
    path('post/', views.post_list, name='post_list'),
    path('login/', login, name='login'),
    path('logout/', logout, {'next_page': 'base'}, name='logout'),
    path('gallery/', include("gallery.urls")),
]
