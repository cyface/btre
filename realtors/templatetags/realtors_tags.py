from django import template
from realtors.models import Realtor

register = template.Library()


@register.inclusion_tag('realtors/templatetags/_realtor_tile.html')
def realtor_tile(realtor):
    return {'realtor': realtor}


@register.inclusion_tag('realtors/templatetags/_realtor_tile.html')
def realtor_of_the_month_tile():
    return {'realtor': Realtor.objects.filter(is_mvp=True).first(), 'mvp': True}
