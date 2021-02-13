from django import template
from ..models import *

register  = template.Library()

@register.inclusion_tag("base.html")
def category_navbor():
    return{
        'categories' : Category.objects.all()
    }