from django.urls import path, include
from django.contrib import admin
from blog.views import BaseView
# base, category
    # , obtain_countries
    # , search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('blog/', include('blog.urls')),
                  path('users/', include('users.urls')),
                  # path('users/', include('django.contrib.auth.urls')),
                  path('gallery/', include('gallery.urls')),
                  path('', BaseView.as_view(), name='base'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
