from django import forms
from rides.models import Ride, RideReview
from django.utils import timezone
from common import choices


class RideBaseForm(forms.ModelForm):

    road_types = forms.MultipleChoiceField(choices = choices.RoadTypeChoices.choices, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Ride
        fields = (
            'title',
            'ride_organizer',
            'meeting_point',
            'city',
            'custom_city_or_village',
            'destination',
            'departure_date',
            'estimated_duration_hours',
            'distance',
            'road_types',
            'road_difficulty',
            'status',
            'maximum_riders_to_join',
            'description'
        )

        labels = {
            'title': 'Ride Title',
            'ride_organizer': 'Ride Organizer',
            'meeting_point': 'Meeting Point',
            'city': 'City',
            'custom_city_or_village': 'Custom City or Village',
            'destination': 'Destination',
            'departure_date': 'Departure Date and Time',
            'estimated_duration_hours': 'Estimated Duration - Total Hours',
            'distance': 'Distance in km',
            'road_types': 'Road Types',
            'road_difficulty': 'Road Difficulty',
            'status': 'Status of the ride',
            'maximum_riders_to_join': 'Maximum number of Riders to Join',
            'description': 'Description of the ride',
        }

        help_texts = {
            'title': 'Provide a title of the ride, at least 5 characters',
            'ride_organizer': 'Name/nickname of the ride organizer',
            'meeting_point': 'Provide meeting point (address), at least 5 characters',
            'city': 'Provide name of the city or village where the ride starts',
            'custom_city_or_village': 'Provide name of the city or village where ride starts, required only if you have selected Other in the field above',
            'destination': 'Provide name of the ride destination, at least 5 characters',
            'departure_date': 'Provide departure date and time',
            'estimated_duration_hours': 'Provide estimated duration in total hours',
            'distance': 'Provide total km distance of the ride',
            'road_types': 'Select road types applicable for the ride',
            'road_difficulty': 'Select road difficulty',
            'status': 'Provide status of the ride',
            'maximum_riders_to_join': 'Provide maximum number of riders to join',
            'description': 'Provide description of the ride',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Provide a title for the ride'}),
            'ride_organizer': forms.Select(),
            'meeting_point': forms.TextInput(attrs={'placeholder': 'Provide meeting point - address'}),
            'city': forms.Select(),
            'custom_city_or_village': forms.TextInput(attrs={'placeholder': 'Provide name of the city or village'}),
            'destination': forms.TextInput(attrs={'placeholder': 'Provide name of the destination'}),
            'departure_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'estimated_duration_hours': forms.NumberInput(attrs={'min': 1}),
            'distance': forms.NumberInput(attrs={'min': 1}),
            # 'road_types': forms.Select(),
            'road_difficulty': forms.Select(),
            'status': forms.Select(),
            'maximum_riders_to_join': forms.NumberInput(attrs={'min': 1}),
            'description': forms.Textarea(
                attrs={
                    'rows': 5,
                    'placeholder': 'Provide description of the ride, stops, fuel stations, etc - things other riders are good to know'}),

        }

    def clean(self):
        cleaned_data = super().clean()

        city = cleaned_data.get('city')
        custom_city_or_village = cleaned_data.get('custom_city_or_village')

        if city == choices.BulgarianCityChoices.OTHER and not custom_city_or_village:
            self.add_error('custom_city_or_village', 'Please provide a city or a village name.')

        return cleaned_data

    def clean_departure_date(self):
        departure_date = self.cleaned_data['departure_date']

        if departure_date < timezone.now():
            raise forms.ValidationError('Departure Date must be in the future.')

        return departure_date

    def clean_road_types(self):
        road_types = self.cleaned_data['road_types']
        return ', '.join(road_types)





# def clean(self):
#     cleaned_data = super().clean()
#
#     city = cleaned_data.get('city')
#     custom_city = cleaned_data.get('custom_city_or_village')
#
#     if city == 'Other' and not custom_city:
#         self.add_error(
#             'custom_city_or_village',
#             'Please provide the city or village name.'
#         )
#
#     return cleaned_data

class RideCreateForm(RideBaseForm):
    pass


class RideEditForm(RideBaseForm):
    pass


class RideDeleteForm(RideBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True

