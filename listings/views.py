from django.views.generic import TemplateView, DetailView, ListView

from .models import Listing


class ListingsView(ListView):
    """
    Shows listings page
    """
    model = Listing
    template_name = "listings/listings.html"
    context_object_name = "listings"
    paginate_by = 3


class ListingView(DetailView):
    """
    Shows listing detail page
    """
    model = Listing
    template_name = "listings/listing.html"


class SearchView(TemplateView):
    """
    Shows search results page
    """
    template_name = "listings/search.html"
