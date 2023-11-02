from django import template
# from django.forms.models import model_to_dict
import json

register = template.Library()

@register.filter
def getvalue(value):
    return json.dumps(value)


@register.filter
def convert_str (v, ) :
    try :
        if str(v, )[0]=="/":
           return True
        else:
           return False
    except ValueError :
     return v


# @register.filter
# def getvalue(value):
#     for i in range(1,11):
#         value[i] = (model_to_dict(value[i]))
#     value['match'] = model_to_dict(value['match'])
#     return json.dumps(value)