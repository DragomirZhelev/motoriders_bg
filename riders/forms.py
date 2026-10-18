from django import forms

from common import choices
from riders.models import Rider

class RiderBaseForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = (
            'first_name',
            'last_name',
            'nickname',
            'city',
            'custom_city_or_village',
            'motorcycle_brand',
            'motorcycle_model',
            'motorcycle_type',
            'experience_years',
            'phone_number',
            'email',
            'motorcyclist_image',
            'short_bio',

        )

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'nickname': 'Nickname',
            'city': 'City',
            'custom_city_or_village': 'Custom City or Village',
            'motorcycle_brand': 'Motorcycle Brand',
            'motorcycle_model': 'Motorcycle Model',
            'motorcycle_type': 'Motorcycle Type',
            'experience_years': 'Experience Years',
            'phone_number': 'Phone Number',
            'email': 'Email Address',
            'motorcyclist_image': 'Profile Photo',
            'short_bio': 'Short Bio',
        }

        help_texts = {
            'first_name': 'Names shall contain only letters',
            'last_name': 'Names shall contain only letters',
            'nickname': 'Nickname shall be unique and at least 3 characters long',
            'city': 'Select a city',
            'custom_city_or_village': 'Enter name of the city or village in case "Other" is selected from above',
            'motorcycle_brand': 'Provide the motorcycle brand for your machine',
            'motorcycle_model': 'Provide the motorcycle model for your machine',
            'motorcycle_type': 'Select the motorcycle type for your machine',
            'experience_years': 'Provide the number of experience years you have riding a motorcycle',
            'phone_number': 'Phone numbers shall contain only digits',
            'email': 'Email is optional',
            'motorcyclist_image': 'Upload a profile photo',
            'short_bio': 'Provide a short bio if you want - maximum 500 characters',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'enter your last name'}),
            'nickname': forms.TextInput(attrs={'placeholder': 'enter your nickname'}),
            'city': forms.Select(),
            'custom_city_or_village': forms.TextInput(attrs={'placeholder': 'enter city or village name'}),
            'motorcycle_brand': forms.TextInput(attrs={'placeholder': 'enter your motorcycle brand'}),
            'motorcycle_model': forms.TextInput(attrs={'placeholder': 'enter your motorcycle model'}),
            'motorcycle_type': forms.Select(),
            'experience_years': forms.NumberInput(attrs={'min': 0}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'enter your phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'enter your email address'}),
            'short_bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell others about yourself....'}),
        }


        error_messages = {
            'first_name': {'required': 'Please, provide your first name',
                           'max_length': 'First name can not be more than 50 characters'},
            'last_name': {'required': 'Please, provide your last name',
                          'max_length': 'Last name can not be more than 50 characters'},

            'nickname': {'required': 'Please, provide your nickname',
                         'max_length': 'Nickname can not be more than 50 characters',
                         'unique': 'Nickname must be unique'},

            'city': {'required': 'Please, select your city',
                     'invalid_choice': 'Please select a valid city'},

            'custom_city_or_village': {'max_length': 'Name of city or village can not be more than 100 characters',},

            'motorcycle_brand': {'required': 'Please, provide your motorcycle brand',
                                 'max_length': 'Motorcycle brand can not be more than 50 characters'},

            'motorcycle_model': {'required': 'Please, provide your motorcycle model',
                                 'max_length': 'Motorcycle model can not be more than 50 characters'},

            'motorcycle_type': {'required': 'Please, select your motorcycle type',
                                'invalid_choice': 'Please, select a valid motorcycle type'},

            'experience_years': {'required': 'Please, provide your experience years as rider',
                                 'invalid': 'Please, provide valid number of years between 0 and 100'},
            'phone_number': {'required': 'Please, provide your phone number',
                             'invalid': 'Phone number must contain only digits',},

            'email': {'invalid': 'Please, provide a valid email address',},

            'motorcyclist_image': {'invalid': 'Please, provide a valid motorcyclist image file',},

            'short_bio': {'max_length': 'Short bio text can not be more than 500 characters',},
        }


    def clean(self):
        cleaned_data = super().clean()

        city = cleaned_data.get('city')
        custom_city_or_village = cleaned_data.get('custom_city_or_village')

        if city == choices.BulgarianCityChoices.OTHER and not custom_city_or_village:
            self.add_error('custom_city_or_village', 'Please provide a city or a village name if Other is selected in the field above.')

        return cleaned_data

class RiderCreateForm(RiderBaseForm):
    pass



class RiderEditForm(RiderBaseForm):
    pass


class RiderDeleteForm(RiderBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True




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