from django.db import models
from schools.models import School


class Room(models.Model):

    school = models.ForeignKey(School, null=False,
                               blank=False, on_delete=models.CASCADE,
                               related_name='rooms')
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    icon = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
