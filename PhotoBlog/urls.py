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
from django.contrib import admin
from django.contrib.auth import views
from blog.views import base, category
    # , obtain_countries
    # , search
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, {'next_page': "base"}, name='logout'),
    # url(r'^search/$', search, name='search'),
    url(r'^$', base, name='base'),

    # url(r'^obtain_countr.+/(?P<pk>\d+)?$', obtain_countries, name="obtain_countries"),
    url(r'', include('blog.urls'))]
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
