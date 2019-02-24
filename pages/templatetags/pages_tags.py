from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active_class_if_path(context, path):
    if path == context.request.path:
        return "active"
    else:
        return None
