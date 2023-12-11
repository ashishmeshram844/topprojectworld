from django import template

register = template.Library()

@register.simple_tag
def get_in_rupees(paisa):
    paisa = float(paisa)
    in_rs = paisa/100
    in_rs = float(in_rs)
    return in_rs