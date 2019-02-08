from django.urls import path

from .views import ListingView, ListingsView, SearchView

urlpatterns = [
    path('', ListingsView.as_view(), name='listings'),
    path('<int:pk>', ListingView.as_view(), name='listing'),
    path('search', SearchView.as_view(), name='search'),
]
