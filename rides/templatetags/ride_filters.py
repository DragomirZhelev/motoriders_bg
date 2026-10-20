from django import template

register = template.Library()

@register.filter
def count_participants(ride):
    return ride.participants.count()

@register.filter
def remaining_slots(ride):
    result = ride.maximum_riders_to_join - ride.participants.count()
    return result

@register.filter
def status_of_the_ride_color(status):
    if status == 'Planned':
        return '\U0001F7E2 Planned'
    elif status == 'Completed':
        return '\U0001F535 Completed'
    elif status == 'Cancelled':
        return '\U0001F534 Canceled'

    return status

