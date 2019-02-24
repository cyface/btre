"""
Accounts Views
"""
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from accounts.forms import RegisterForm


class DashboardView(TemplateView):
    """
    Shows Dashboard Page
    """
    template_name = "accounts/dashboard.html"


class RegisterView(FormView):
    """
    Shows Register Page
    """
    form_class = RegisterForm
    template_name = "accounts/register.html"

    def form_valid(self, form):
        login(self.request, form.user)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
