from django import template

register = template.Library()

@register.simple_tag
def multiply(price, exchange_rate, *args, **kwargs):
    rate = price * exchange_rate   
    return int(rate) #round(int(rate),-2)