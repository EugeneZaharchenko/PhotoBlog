from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/category/<int:pk>/', views.category, name="category"),
    path('post/tag/<int:pk>/', views.tag, name='tag'),
    path('post/search/', views.search, name='search'),
    path('post/', views.post_list, name='post_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', include("users.urls")),
    path('gallery/', include("gallery.urls")),
]
