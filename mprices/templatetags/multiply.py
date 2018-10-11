from django import template

register = template.Library()

@register.simple_tag
def multiply(usd, exchange_rate, *args, **kwargs):
    rate = usd * exchange_rate
    return int(rate) #round(int(rate),-2)