
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from common.mixins import TimeStamp
from riders.models import Rider
from common import choices




# Create your models here.
class HelpRequest(TimeStamp):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='help_requests')
    title = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    issue_description = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(2000) ])
    urgency = models.CharField(max_length=10, choices = choices.UrgencyChoices.choices)
    location = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    status = models.CharField(max_length=20, choices = choices.HelpRequestStatusChoices.choices)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title} - {self.status} - {self.rider.nickname}'

    class Meta:
        ordering = ('-created_at',)
