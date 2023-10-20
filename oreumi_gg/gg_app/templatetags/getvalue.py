from django import template

register = template.Library()

@register.filter
def getvalue(list, index):
    return list[index]