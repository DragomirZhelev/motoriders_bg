from django.contrib import admin
from rides.models import Ride, RideReview
# Register your models here.

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ['title', 'ride_organizer',]
    list_filter = ['title', 'ride_organizer',]
    search_fields = ['title', 'ride_organizer__nickname']


@admin.register(RideReview)
class RideReviewAdmin(admin.ModelAdmin):
    list_display = ['ride', 'get_reviewer_nickname']


    def get_reviewer_nickname(self, obj):
        return obj.reviewer.nickname