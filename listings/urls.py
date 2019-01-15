from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListingsView.as_view(), name='listings'),
    path('<int:listing_id>', views.ListingView.as_view(), name='listing'),
    path('search', views.SearchView.as_view(), name='search'),
]
