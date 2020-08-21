from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import auth_login, auth_logout
from blog.views import HomePageView, AboutView
    # , category
    # , obtain_countries
    # , search
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', auth_login, name='login'),
    path('logout/', auth_logout, {'next_page': "base"}, name='logout'),
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='base'),
    path('gallery/', include("gallery.urls")),
    path('about/', AboutView.as_view(), name='about'),
    path('', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

