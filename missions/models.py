from django.db import models
from rest_framework.exceptions import ValidationError

from spy_cats.models import SpyCats


class Missions(models.Model):
    cat = models.ForeignKey(SpyCats, null=True, blank=True, on_delete=models.PROTECT, related_name='missions')
    is_completed = models.BooleanField(default=False, null=False, blank=False)

    def save(self, *args, **kwargs):
        if self.cat:
            uncompleted_missions = self.cat.missions.filter(is_completed=False).exclude(id=self.id)
            if uncompleted_missions.exists():
                raise ValidationError('One cat can have only one active mission')
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.cat:
            raise ValidationError('Can not be deleted if a cat is already assigned')
        return super().delete(*args, **kwargs)


class Targets(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    notes = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    mission = models.ForeignKey(Missions, on_delete=models.PROTECT, related_name='targets')

    def save(self, *args, **kwargs):
        if self.mission.targets.filter(is_completed=False).count() == 0:
            self.mission.is_completed = True
            self.mission.save()
        return super().save(*args, **kwargs)
