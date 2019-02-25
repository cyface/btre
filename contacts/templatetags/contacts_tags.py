from django import template

from contacts.forms import ContactForm

register = template.Library()


def set_user_values(user):
    initial = {}
    if user:
        initial['user_id'] = user.id
        initial['name'] = user.get_full_name()
        initial['email'] = user.email
    return initial


@register.inclusion_tag('contacts/partials/_inquiry_form.html')
def contact_form(user=None):
    initial = set_user_values(user)
    return {'form': ContactForm(initial=initial)}


@register.inclusion_tag('contacts/templatetags/_inquiry_modal.html')
def inquiry_modal(listing=None, user=None):
    initial = set_user_values(user)
    if listing:
        initial['listing'] = listing.title
        initial['listing_id'] = listing.id
    return {'form': ContactForm(initial=initial)}
