from django import template

from core.models import HeaderCategory

register = template.Library()


@register.simple_tag
def header_category():
    header = HeaderCategory.objects.all()
    return header