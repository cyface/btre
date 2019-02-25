from django import template

from contacts.forms import ContactForm

register = template.Library()


@register.inclusion_tag('contacts/partials/_inquiry_form.html')
def contact_form(user=None):
    initial = {}
    if user:
        initial['user_id'] = user.id
    return {'form': ContactForm(initial=initial)}


@register.inclusion_tag('contacts/templatetags/_inquiry_modal.html')
def inquiry_modal(listing=None, user=None):
    initial = {}
    if listing:
        initial['listing'] = listing.title
        initial['listing_id'] = listing.id
    if user:
        initial['user_id'] = user.id
    return {'form': ContactForm(initial=initial)}
