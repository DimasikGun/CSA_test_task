# Generated by Django 5.1.4 on 2024-12-14 11:47

import spy_cats.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpyCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('years_of_experience', models.PositiveSmallIntegerField(default=0)),
                ('breed', models.CharField(max_length=100, validators=[spy_cats.validators.validate_breed])),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
