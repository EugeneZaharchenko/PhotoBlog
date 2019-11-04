from django.urls import path, include
from django.contrib import admin
from blog.views import BaseView, contacts
# base, category
    # , search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('blog/', include('blog.urls'), name='blog'),
                  path('contacts/', contacts, name='contacts'),
                  path('users/', include('users.urls')),
                  # path('users/', include('django.contrib.auth.urls')),
                  path('gallery/', include('gallery.urls'), name='gallery'),
                  path('', BaseView.as_view(), name='home'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
