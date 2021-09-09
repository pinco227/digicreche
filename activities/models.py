from django.db import models
from pupils.models import Pupil


class ActivityType(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    icon = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Activity(models.Model):

    type = models.ForeignKey(ActivityType, null=True, blank=False,
                             on_delete=models.SET_NULL)
    description = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pupil = models.ForeignKey(Pupil, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='activities')

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.type.name
