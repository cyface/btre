"""
Contacts Views
"""
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from contacts.forms import ContactForm
from contacts.models import Contact


class ContactFormView(FormView):
    """
    Shows Contact Form
    """
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')
    template_name = "contacts/contact_form.html"

    def form_valid(self, form):
        """
        Process contact form
        """
        Contact.objects.create(**form.cleaned_data)  # ** explodes dictionary into kwargs
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    """
    Shows Contact Success Page
    """
    template_name = "contacts/contact_success.html"
