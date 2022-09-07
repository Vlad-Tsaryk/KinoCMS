from django import template
from cinema.models import *
register = template.Library()


@register.simple_tag()
def get_obj(obj, pk):
    filtered = obj.objects.distinct()
    return filtered
