from django.core.exceptions import ValidationError

def validate_names_only_letters(value): # add help_text: Names may contain only letters, no digits, no punctuation, no special symbols in the form
    if not value.isalpha():
        raise ValidationError("Names may contain only letters, no digits, no punctuation, no special symbols!")



def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError("Phone numbers may contain only digits")