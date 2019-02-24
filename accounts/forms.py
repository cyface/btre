from django import forms
from django.contrib.auth.models import User
from django.db import IntegrityError


class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True)
    first_name.widget.attrs.update({'class': 'form-control'})

    last_name = forms.CharField(required=True)
    last_name.widget.attrs.update({'class': 'form-control'})

    username = forms.CharField(required=True)
    username.widget.attrs.update({'class': 'form-control'})

    email = forms.CharField(required=True)
    email.widget.attrs.update({'class': 'form-control'})

    password = forms.CharField(required=True, widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'form-control'})

    user = None

    def clean(self):
        try:
            user = User.objects.create_user(self.cleaned_data.get('username'), self.cleaned_data.get('email'), self.cleaned_data.get('password'))
            user.last_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.save()
            self.user = user
            return True
        except IntegrityError:
            return False
