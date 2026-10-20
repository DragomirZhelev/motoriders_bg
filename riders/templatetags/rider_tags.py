from django import template

register = template.Library()

@register.simple_tag
def number_of_reviews_per_rider(rider):
    return rider.written_reviews.count()

@register.simple_tag
def number_organized_rides(rider):
    return rider.rides.count()