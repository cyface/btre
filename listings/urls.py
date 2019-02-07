from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.ListingsView.as_view(), name='listings'),
    path('<int:listing_id>', views.ListingView.as_view(), name='listing'),
    path('search', views.SearchView.as_view(), name='search'),
]
