from django.db import models
from schools.models import School
from django.contrib.auth import get_user_model


class Room(models.Model):

    school = models.ForeignKey(School, null=False,
                               blank=False, on_delete=models.CASCADE,
                               related_name='school')
    name = models.CharField(max_length=255, unique=True,
                            null=False, blank=False)
    description = models.TextField()
    email = models.EmailField(max_length=255, unique=True)
    teacher = models.OneToOneField(get_user_model(), null=True,
                                   blank=False, on_delete=models.SET_NULL,
                                   related_name='teacher')

    def __str__(self):
        return self.name
