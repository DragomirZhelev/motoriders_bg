from django.contrib import admin
from riders.models import Rider


# Register your models here.

@admin.register(Rider)
class Rider(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'nickname',
        'city',
        'motorcycle_brand',
        'motorcycle_type'
    ]

    list_filter = [
        'first_name',
        'last_name',
        'nickname',
        'city',
        'motorcycle_brand',
        'motorcycle_type'
    ]

    search_fields = [
        'first_name',
        'last_name',
        'nickname',
        'city',
        'motorcycle_brand',
        'motorcycle_type'
    ]



# Register your models here.
