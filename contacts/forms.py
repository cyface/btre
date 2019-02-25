from django import forms


class ContactForm(forms.Form):
    label_suffix = ''

    email = forms.CharField(max_length=50)
    email.widget.attrs.update({'class': 'form-control'})

    listing = forms.CharField(max_length=200)
    listing.widget.attrs.update({'class': 'form-control'})

    listing_id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    listing_id.widget.attrs.update({'class': 'form-control'})

    message = forms.CharField(required=False, widget=forms.TextInput)
    message.widget.attrs.update({'class': 'form-control'})

    name = forms.CharField(max_length=200)
    name.widget.attrs.update({'class': 'form-control'})

    phone = forms.CharField(max_length=20)
    phone.widget.attrs.update({'class': 'form-control'})

    user_id = forms.IntegerField(required=False, widget=forms.HiddenInput)
