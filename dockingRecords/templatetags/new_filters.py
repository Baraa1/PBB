from django import template
import datetime

register = template.Library()

# for FIDS page
@register.filter('get_value')
def get_value(diction, key):
    if diction:
        try:
            return diction[key]
        except:
            return 'N/A'

@register.filter(name='unix_to_datetime')
def unix_to_datetime(diction, key):
    if diction:
        try:
            return datetime.datetime.fromtimestamp(int(diction[key]))
        except:
            return 'N/A'
        

@register.filter(name='start_from')
def start_from(value, arg):
    """
    Returns a sliced list, starting from the given index.
    """
    try:
        index = int(arg)
        return value[index:]
    except (ValueError, IndexError):
        return value