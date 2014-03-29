from django.template import Library
from django.core.exceptions import ObjectDoesNotExist

register = Library()

@register.filter
def get(models, argstring):
    args = argstring.split(',')
    if len(args) != 2:
        raise ValueError("Exactly two arguments required, separated by comma")
    field, value = args
    try:
        return models.get(**{field: value})
    except ObjectDoesNotExist:
        return None
