from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import auth_login, auth_logout
from blog.views import base, category
    # , obtain_countries
    # , search
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = [
#     # url(r'^search/$', search, name='search'),

urlpatterns = [
    path('login/', auth_login, name='login'),
    path('logout/', auth_logout, {'next_page': "base"}, name='logout'),
    path('admin/', admin.site.urls),
    path('', base, name='base'),
    path('gallery/', include("gallery.urls")),
    path('', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

