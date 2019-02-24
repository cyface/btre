"""
Accounts Views
"""
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
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
        """
        Assuming that all the validations ran clean for the RegisterForm,
        create the user, log them in, and show them their dashboard
        There is a teeny possibility of a race condition here where someone else signs up with the same username
        in the microseconds between when we validated that the username was available and when this code runs
        but the chances are minuscule, and they would just end up seeing the 500 page, worst case. ¯\_(ツ)_/¯
        """
        user = User.objects.create_user(form.cleaned_data.get('username'), form.cleaned_data.get('email'), form.cleaned_data.get('password'))
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.save()
        login(self.request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)
