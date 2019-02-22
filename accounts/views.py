"""
Accounts Views
"""
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    """
    Shows Dashboard Page
    """
    template_name = "accounts/dashboard.html"


class RegisterView(TemplateView):
    """
    Shows Register Page
    """
    template_name = "accounts/register.html"
