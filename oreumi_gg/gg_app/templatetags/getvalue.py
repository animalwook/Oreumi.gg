from django import template
import json

register = template.Library()

@register.filter
def getvalue(value):
    return json.dumps(value)