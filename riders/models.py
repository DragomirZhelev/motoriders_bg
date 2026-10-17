from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from common import validators, choices
from common.mixins import TimeStamp, LocationMixin


# Create your models here.
class Rider(TimeStamp, LocationMixin):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(2), validators.validate_names_only_letters],)
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(2), validators.validate_names_only_letters],)
    nickname = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(3)])
    # city = models.CharField(max_length=50, validators=[MinLengthValidator(2)], choices = choices.BulgarianCityChoices.choices,)
    # custom_city_or_village = models.CharField(max_length=100, blank=True)
    motorcycle_brand = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    motorcycle_model = models.CharField(max_length=50)
    motorcycle_type = models.CharField(max_length=50, choices =choices.MotorcycleTypeChoices.choices)
    experience_years = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    phone_number = models.CharField(max_length=50, blank=False, validators=[validators.validate_phone_number])
    email = models.EmailField(blank=True)
    motorcyclist_image = models.ImageField(upload_to='riders_photos/', blank=True)
    short_bio = models.TextField(blank=True, max_length=500)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.nickname}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Riders'
        verbose_name = 'Rider'
        ordering = ['-created_at']