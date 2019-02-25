"""
Accounts Views
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """
    Form to Log Users In - Only subclassing to be able to add Bootstrap CSS Class
    """

    def __init__(self, request=None, *args, **kwargs):
        self.declared_fields['username'].widget.attrs.update({'class': 'form-control'})
        self.declared_fields['password'].widget.attrs.update({'class': 'form-control'})
        kwargs['label_suffix'] = ''
        super().__init__(request, *args, **kwargs)


class RegisterForm(forms.Form):
    label_suffix = ''

    first_name = forms.CharField(required=True, label="First Name")
    first_name.widget.attrs.update({'class': 'form-control'})

    last_name = forms.CharField(required=True, label="Last Name")
    last_name.widget.attrs.update({'class': 'form-control'})

    username = forms.CharField(required=True)
    username.widget.attrs.update({'class': 'form-control'})

    email = forms.EmailField(required=True)
    email.widget.attrs.update({'class': 'form-control'})

    password = forms.CharField(required=True, widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'form-control'})

    password_validate = forms.CharField(required=True, widget=forms.PasswordInput, label="Password Again")
    password_validate.widget.attrs.update({'class': 'form-control'})

    def clean_password_validate(self):
        """
        Validate that the password and password_validate fields match.
        Since clean_<fieldname> methods are run in order of definition on this class, we check it here rather than on password,
        so that the base type coercions and validations will already have been run for both.
        """
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_validate'):
            self.add_error('password', "Passwords Must Match")  # Adding this as a validation fail on password so the error is attached to that field
        else:
            return self.cleaned_data.get('password_validate')

    def clean_username(self):
        """
        Validate that the username does not already exist
        """
        if User.objects.filter(username=self.cleaned_data.get('username')).exists():
            self.add_error('username', "This Username Already Exists, Please Choose a Different One")
        else:
            return self.cleaned_data.get('username')
