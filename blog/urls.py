from django.urls import path, include
from . import views

urlpatterns = [
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/category/<int:pk>/', views.CategoriesView.as_view(), name='category'),
    path('post/category/<int:pk>/', views.category, name='category'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('post/search/', views.search, name='search'),
    path('', views.post_list, name='blog'),
    # path('posts/', views.post_list, name='posts_list'),
    # path('posts/', views.PostListView.as_view(), name='post_list')
]
