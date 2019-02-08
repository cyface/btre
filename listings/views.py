from django.views.generic import TemplateView, DetailView, ListView

from .models import Listing


class ListingsView(ListView):
    """
    Shows listings list page
    """
    context_object_name = "listings"
    model = Listing
    paginate_by = 3
    template_name = "listings/listings.html"


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
