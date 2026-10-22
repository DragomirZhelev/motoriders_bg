from django import forms

from riders.models import Rider
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
            'estimated_duration_hours': 'Provide estimated duration hours of the ride',
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
            'estimated_duration_hours': forms.NumberInput(attrs={'min': 1.00}),
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


        error_messages = {
            'title': {'required': 'Please, provide a title for the ride',
                      'max_length': 'Title of the ride can not be more than 200 characters.'},
            'ride_organizer': {'required': 'Please, select the ride organizer',
                               'invalid_choice': 'Please, select a valid rider as organizer'},
            'meeting_point': {'required': 'Please, provide the meeting point',
                              'max_length': 'Meeting point can not be more than 50 characters.'},
            'city': {'required': 'Please, select the name of the city or village',
                     'invalid_choice': 'Please, select a valid city or village'},
            'custom_city_or_village': {'max_length': 'Name of city or village cannot be more than 100 characters.'},

            'destination': {'required': 'Please, provide the name of the destination for the ride',
                            'max_length': 'Destination name can not be more than 150 characters.'},
            'departure_date': {'required': 'Please, provide departure date and time',
                               'invalid': 'Please, provide a valid data and time in the future'},
            'estimated_duration_hours': {'required': 'Please, provide estimated duration hours',
                                         'invalid': 'Duration hours can not be less than 1.00'},
            'distance': {'required': 'Please, provide total km distance',
                         'invalid': 'Enter valid distance for the ride between 1 and 10000'},
            'road_types':{'required': 'Please, select at least 1 road type',
                          'invalid_choice': 'Please, select only valid choices'},
            'road_difficulty':{'required': 'Please, select a difficulty level',
                               'invalid_choice': 'Please, select a valid road difficulty'},

            'status': {'required': 'Please, select the status of the ride',
                       'invalid_choice': 'Please, select a valid status choice'},
            'maximum_riders_to_join': {'required': 'Please, select maximum number of riders to join',
                                       'invalid': 'Please, enter a valid number between 1 and 100'},

            'description': {'required': 'Please, provide a description of the ride',
                            'min_length': 'Description must be more than 20 characters',
                            'max_length': 'Description must be less than 500 characters'},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.road_types:
            road_types_as_list = self.instance.road_types.split(',')
            stripped_road_types = [road_type.strip() for road_type in road_types_as_list]
            self.initial['road_types'] = stripped_road_types




    def clean(self):
        cleaned_data = super().clean()

        city = cleaned_data.get('city')
        custom_city_or_village = cleaned_data.get('custom_city_or_village')

        if custom_city_or_village:
            custom_city_or_village = custom_city_or_village.strip()
            cleaned_data['custom_city_or_village'] = custom_city_or_village

        if city == choices.BulgarianCityChoices.OTHER and not custom_city_or_village:
            self.add_error('custom_city_or_village', 'Please provide a city or a village name if Other is selected in the field above.')

        if city != choices.BulgarianCityChoices.OTHER and custom_city_or_village:
            self.add_error('custom_city_or_village', 'You can not use this field "Custom city or village" when a city different than OTHER is selected')

        return cleaned_data

    def clean_departure_date(self):
        departure_date = self.cleaned_data['departure_date']

        if departure_date < timezone.now():
            raise forms.ValidationError('Departure Date must be in the future.')

        return departure_date

    def clean_road_types(self):
        road_types = self.cleaned_data['road_types']
        return ', '.join(road_types)




class RideCreateForm(RideBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status'].choices = [(choices.TripStatusChoices.PLANNED, choices.TripStatusChoices.PLANNED ),]


class RideEditForm(RideBaseForm):
    pass


class RideDeleteForm(RideBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True



class RideReviewBaseForm(forms.ModelForm):
    class Meta:
        model = RideReview

        fields = [
            'ride',
            'reviewer',
            'overall_rating',
            'road_condition_rating',
            'scenery_rating',
            'riding_difficulty',
            'review_text'
        ]

        labels = {
            'ride': 'Ride',
            'reviewer': 'Reviewer',
            'overall_rating': 'Overall Rating',
            'road_condition_rating': 'Road Condition Rating',
            'scenery_rating': 'Scenery Rating',
            'riding_difficulty': 'Riding Difficulty',
            'review_text': 'Review of the ride'
        }

        help_texts = {
            'ride': 'Select the Ride to provide review for',
            'reviewer': 'Select rider providing the review',
            'overall_rating': 'Provide a rate for the ride from 1 to 10',
            'road_condition_rating': 'Provide a rate for the road conditions from 1 to 10',
            'scenery_rating': 'Provide a rate for the scenery from 1 to 10',
            'riding_difficulty': 'Select the riding difficulty.',
            'review_text': 'Provide a short ride review comments up to 500 characters.',
        }


        widgets = {
            'ride': forms.Select(),
            'reviewer': forms.Select(),
            'overall_rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'road_condition_rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'scenery_rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'riding_difficulty': forms.Select(),
            'review_text': forms.Textarea(attrs={'rows': 5, 'placeholder':'Provide your review for the ride'}),
        }

        error_messages = {
            'ride': {'required': 'Please, select the ride you want to provide a review for.',
                     'invalid_choice': 'Please, select a valid ride you want to provide a review for.'},
            'reviewer': {'required': 'Please, select the rider providing the review.',
                        'invalid_choice':'Please, select a valid rider providing the review.'},
            'overall_rating': {'required': 'Please, provide an overall rating from 1 to 10',
                               'invalid': 'Overall rating shall contain valid number between 1 and 10.'},
            'road_condition_rating': {'required': 'Please, provide a rate for the road conditions from 1 to 10',
                                      'invalid': 'Road condition shall contain valid number between 1 and 10.'},
            'scenery_rating': {'required': 'Please, provide a rate for the scenery from 1 to 10',
                               'invalid': 'Scenery shall contain valid number between 1 and 10.'},
            'riding_difficulty': {'required': 'Please, select the riding difficulty.',
                                  'invalid_choice': 'Please, select a valid choice from the drop down'},
            'review_text': {'required': 'Please, provide a short ride review up to 500 characters.',
                            'min_length': 'Ride review text must be at least 20 characters long.',
                            'max_length': 'Ride review text must be less than 500 characters long.'},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ride'].queryset = Ride.objects.filter(status=choices.TripStatusChoices.COMPLETED)


    def clean(self):
        cleaned_data = super().clean()

        reviewer = cleaned_data.get('reviewer')
        ride = cleaned_data.get('ride')

        if ride.status != choices.TripStatusChoices.COMPLETED:
            raise forms.ValidationError('Reviews shall be submitted for rides with status COMPLETED only')

        organizer = ride.ride_organizer
        participants = ride.participants.all()

        if reviewer not in participants and reviewer != organizer:
            raise forms.ValidationError('Only the organizer of the ride or the participants can submit a review')

        return cleaned_data


class RideReviewCreateForm(RideReviewBaseForm):
    pass

class RideReviewEditForm(RideReviewBaseForm):
    pass


class RideReviewDeleteForm(RideReviewBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True




class JoinRideForm(forms.Form):
    rider = forms.ModelChoiceField(
        queryset=Rider.objects.all(),
        label='Rider',
        help_text='Select the rider to join the ride',
        widget=forms.Select(),
        error_messages={'required': 'Please, select the rider to join the ride.',
                        'invalid_choice': 'Please, select a valid rider to join the ride.'},
    )

