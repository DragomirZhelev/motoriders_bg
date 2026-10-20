from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, MaxLengthValidator
from django.db import models

from common.mixins import TimeStamp, LocationMixin
from riders.models import Rider
from common import choices


# Create your models here.
class Ride(TimeStamp, LocationMixin):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    ride_organizer = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='rides' )
    participants = models.ManyToManyField(Rider, related_name='ride_participants', blank=True)
    meeting_point = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    # city = models.CharField(max_length=50, validators=[MinLengthValidator(3)], choices=choices.BulgarianCityChoices.choices)
    # custom_city_or_village = models.CharField(max_length=100, blank=True)
    destination = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    departure_date = models.DateTimeField()
    estimated_duration_hours = models.DecimalField(max_digits=4, decimal_places=2, validators =[MinValueValidator(1.00), MaxValueValidator(500.00)])
    distance = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    road_types = models.CharField(max_length=200)
    road_difficulty = models.CharField(max_length=100, choices = choices.RoadDifficultyChoices.choices)
    status = models.CharField(max_length=50, choices=choices.TripStatusChoices.choices, blank = False, null = False)
    maximum_riders_to_join = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField(validators=[MinLengthValidator(20), MaxLengthValidator(500)])
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# ADD TO THE SEARCH FOR:
# rides = Ride.objects.filter(
#     Q(title__icontains=query) |
#     Q(meeting_point__icontains=query) |
#     Q(destination__icontains=query) |
#     Q(road_types__icontains=query)
# )


class RideReview(TimeStamp):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='ride_reviews')
    reviewer = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='written_reviews')
    overall_rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    road_condition_rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    scenery_rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    riding_difficulty = models.CharField(max_length=100, choices =choices.RidingDifficultyChoices.choices)
    review_text = models.TextField(validators=[MinLengthValidator(20), MaxLengthValidator(500)])
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ride.title} - author: {self.reviewer.nickname}'

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['ride', 'reviewer'],
                name = 'unique_ride_review',
            )
        ]
# Only participants or the organizer can review a ride. ADD TO FORM