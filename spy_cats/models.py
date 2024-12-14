from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from spy_cats.validators import validate_breed


class SpyCats(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    years_of_experience = models.PositiveSmallIntegerField(null=False, blank=False, default=0,
                                                           validators=[MaxValueValidator(40,
                                                                                         message='Cats don`t live so long(')])
    breed = models.CharField(max_length=100, null=False, blank=False, validators=[validate_breed])
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0,
                                 validators=[MinValueValidator(0,
                                                               message='Salary cant be negative')])

    def __str__(self):
        return f'{self.name}({self.breed}) - {self.years_of_experience}'
