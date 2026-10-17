


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