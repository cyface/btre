from django.views.generic import TemplateView, DetailView


class ListingsView(TemplateView):
    """
    Shows listings page
    """
    template_name = "listings/listings.html"


class ListingView(DetailView):
    """
    Shows listing detail page
    """
    # model = Listing
    template_name = "listings/listing.html"


class SearchView(TemplateView):
    """
    Shows search results page
    """
    template_name = "listings/search.html"
