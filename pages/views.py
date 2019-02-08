from django.views.generic import TemplateView

"""
Class way

def index(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/index.html")

"""


class AboutView(TemplateView):
    template_name = "pages/about.html"


class IndexView(TemplateView):
    template_name = "pages/index.html"
