from django import template

register = template.Library()


@register.filter
def overall_rating_color(overall_rating):
    if overall_rating >= 8:
        return '\U0001F7E2 Super Ride'
    elif overall_rating >= 5:
        return '\U0001F7E1 Good Ride'
    else:
        return '\U0001F534 Poor ride'


@register.filter
def road_condition_rating_color(road_condition_rating):
    if road_condition_rating >= 8:
        return '\U0001F7E2 Excellent Road Conditions'
    elif road_condition_rating >= 5:
        return '\U0001F7E1 Good Road Conditions'
    else:
        return '\U0001F534 Poor road conditions'


@register.filter
def scenery_rating_color(scenary_rating):
    if scenary_rating >= 8:
        return '\U0001F7E2 Excellent Scenery'
    elif scenary_rating >= 5:
        return '\U0001F7E1 Good Scenery'
    else:
        return '\U0001F534 Poor Scenery'
