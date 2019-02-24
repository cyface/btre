from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from contacts.views import ContactView

urlpatterns = [
                  path('', include('pages.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('admin/', admin.site.urls),
                  path('contact/', ContactView.as_view(), name='contact'),
                  path('listings/', include('listings.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
