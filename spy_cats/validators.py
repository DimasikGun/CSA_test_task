from rest_framework.exceptions import ValidationError

from spy_cats.breeds_logic import Breeds


def validate_breed(value):
    breed_names = Breeds.get_breeds()
    if value not in breed_names:
        raise ValidationError(f"Invalid breed '{value}'. Please select a valid breed.")
