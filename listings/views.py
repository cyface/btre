from django.views.generic import DetailView, ListView, FormView

from listings.forms import SearchForm
from .models import Listing


class ListingsView(ListView):
    """
    Shows listings list page
    """
    context_object_name = "listings"
    model = Listing
    paginate_by = 3
    queryset = Listing.objects.filter(is_published=True)
    template_name = "listings/listings.html"


class ListingView(DetailView):
    """
    Shows listing detail page
    """
    model = Listing
    template_name = "listings/listing.html"


class SearchView(FormView):
    """
    Shows search results page
    """
    template_name = "listings/search.html"
    form_class = SearchForm
    http_method_names = ['get', 'post']

    def form_valid(self, form):
        context = self.get_context_data()
        listings = Listing.objects.filter(is_published=True).order_by('-list_date')
        if form.cleaned_data.get('keywords'):
            listings = listings.filter(description__contains=form.cleaned_data.get('keywords'))
        if form.cleaned_data.get('city') and form.cleaned_data.get('city') != "ALL":
            listings = listings.filter(city__icontains=form.cleaned_data.get('city'))
        if form.cleaned_data.get('state') and form.cleaned_data.get('state') != "ALL":
            listings = listings.filter(state=form.cleaned_data.get('state'))
        if form.cleaned_data.get('bedrooms') and form.cleaned_data.get('bedrooms') != "ALL":
            listings = listings.filter(bedrooms__gte=form.cleaned_data.get('bedrooms'))
        if form.cleaned_data.get('max_price') and form.cleaned_data.get('max_price') != "ALL":
            listings = listings.filter(price__lte=form.cleaned_data.get('max_price'))
        context['listings'] = listings
        return self.render_to_response(context=context)
