from django import template

register = template.Library()


@register.inclusion_tag('listings/templatetags/_listing_tile.html')
def show_listing_tile(listing):
    return {'listing': listing}


@register.inclusion_tag('listings/templatetags/_listing_photo_thumbnail.html')
def show_photo_thumbnail(photo):
    return {'photo': photo}
