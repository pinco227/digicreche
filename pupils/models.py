from django.db import models
from rooms.models import Room
from schools.models import School
from accounts.models import DigiCrecheUser


class Pupil(models.Model):

    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    personal_details = models.JSONField(null=True, blank=True)
    school = models.ForeignKey(School, null=False,
                               blank=False, on_delete=models.CASCADE,
                               related_name='students')
    room = models.ForeignKey(Room, null=True,
                             blank=False, on_delete=models.SET_NULL,
                             related_name='pupils')
    parents = models.ManyToManyField(DigiCrecheUser, related_name='children')

    def __str__(self):
        return self.name

    def remove_room(self):
        self.room = None
        self.save()
