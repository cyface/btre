from django.views.generic import ListView

from listings.forms import SearchForm
from listings.models import Listing
from realtors.models import Realtor

"""
Class way

def index(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/index.html")

"""


class AboutView(ListView):
    context_object_name = "realtors"
    model = Realtor
    template_name = "pages/about.html"


class IndexView(ListView):
    context_object_name = "listings"
    model = Listing
    queryset = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context
