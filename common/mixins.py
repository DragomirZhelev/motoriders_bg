from typing import cast

from django.core.exceptions import ValidationError
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
    #
    # def clean(self):
    #     super().clean()
    #
    #     if self.custom_city_or_village:
    #         self.custom_city_or_village = self.custom_city_or_village.strip()
    #
    #     if self.city == choices.BulgarianCityChoices.OTHER and not self.custom_city_or_village:
    #         raise ValidationError('Please provide a city or a village name if Other is selected in the field above.')
    #
    #
    #     if self.city != choices.BulgarianCityChoices.OTHER and self.custom_city_or_village:
    #         raise ValidationError('You can not use this field when a city different than OTHER is selected')