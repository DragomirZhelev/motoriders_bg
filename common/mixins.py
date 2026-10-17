from django.core.validators import MinLengthValidator
from django.db import models
from common import choices

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class LocationMixin(models.Model):
    city = models.CharField(max_length=50, validators=[MinLengthValidator(3)], choices=choices.BulgarianCityChoices.choices)
    custom_city_or_village = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True