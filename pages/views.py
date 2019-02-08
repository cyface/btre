from django.views.generic import TemplateView, ListView

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


class IndexView(TemplateView):
    template_name = "pages/index.html"
