"""
Accounts Views
"""
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView

from accounts.forms import RegisterForm, LoginForm


class DashboardView(TemplateView):
    """
    Shows Dashboard Page
    """
    template_name = "accounts/dashboard.html"


class LoginView(DjangoLoginView):
    """
    Subclasses Django's Login View to allow tweaking the login form
    """
    form_class = LoginForm


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
        form.cleaned_data.pop('password_validate')  # create_user doesn't want 'password_validate', so we're removing it
        user = User.objects.create_user(**form.cleaned_data)  # Double-star explodes the dictionary into kwargs
        login(self.request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)
