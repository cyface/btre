from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from accounts.views import RegisterView, DashboardView

urlpatterns = [
                  path('', include('pages.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('admin/', admin.site.urls),
                  path('dashboard/', DashboardView.as_view(), name='dashboard'),
                  path('listings/', include('listings.urls')),
                  path('register/', RegisterView.as_view(), name='register'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
