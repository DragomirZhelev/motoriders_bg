from django import forms
from assistance.models import HelpRequest

class HelpRequestBaseForm(forms.ModelForm):
    class Meta:
        model = HelpRequest

        fields = (
            'rider',
            'title',
            'issue_description',
            'urgency',
            'location',
            'status'
        )

        labels = {
            'rider': 'Rider',
            'title': 'Title',
            'issue_description': 'Issue Description',
            'urgency': 'Urgency',
            'location': 'Location',
            'status': 'Status'
        }

        help_texts = {
            'rider': 'Select the rider that requests assistance',
            'title': 'Provide a short descriptive title of the issue',
            'issue_description': 'Provide an exhaustive description of the issue',
            'urgency': 'Select a level of urgency',
            'location': 'Provide the location where the issue has occurred and help is needed',
            'status': 'Select the status of the help request',
        }

        widgets = {
            'rider': forms.Select(),
            'title': forms.TextInput(attrs={'placeholder': 'Short title of the issue'}),
            'issue_description': forms.Textarea(attrs={'rows': 5 ,'placeholder': ' Exhaustive description of the issue'}),
            'urgency': forms.Select(),
            'location': forms.TextInput(attrs={'placeholder': 'Exact location/address of the issue'}),
            'status': forms.Select(),
        }

        error_messages = {
            'rider': {'required': 'Please, select the rider that needs help',
                      'invalid_choice': 'Please, select a valid rider'},
            'title': {'required': 'Please, provide descriptive title of the issue',
                      'max_length': 'Title of the issue must be less than 100 characters'},
            'issue_description': {'required': 'Please, provide description of the issue',
                                  'min_length': 'Description of the issue must be at least 10 characters',
                                  'max_length': 'Description of the issue must be less than 2000 characters'},
            'urgency': {'required': 'Please, select a level of urgency',
                        'invalid_choice': 'Please, select a valid level of urgency',},
            'location': {'required': 'Please, provide a location',
                         'max_length': 'Location must be less than 100 characters',
                         'min_length': 'Location must be at least 5 characters'},
            'status': {'required': 'Please, select a status',
                       'invalid_choice': 'Please, select a valid status',}

        }

class HelpRequestCreateForm(HelpRequestBaseForm):
    pass

class HelpRequestEditForm(HelpRequestBaseForm):
    pass

class HelpRequestDeleteForm(HelpRequestBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True


