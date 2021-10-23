import os

from accounts.models import DigiCrecheUser
from django.db import models
from django.utils.text import slugify
from rooms.models import Room
from schools.models import School


def get_upload_path(instance, filename):
    pupil_slug = slugify(instance.first_name + ' ' + instance.last_name)
    return os.path.join(
        instance.school.slug,
        pupil_slug,
        filename)


class Pupil(models.Model):

    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    personal_details = models.JSONField(null=True, blank=True)
    school = models.ForeignKey(School, null=False,
                               blank=False, on_delete=models.CASCADE,
                               related_name='students')
    room = models.ForeignKey(Room, null=True,
                             blank=True, on_delete=models.SET_NULL,
                             related_name='pupils')
    parents = models.ManyToManyField(
        DigiCrecheUser, related_name='children', blank=True)
    photo = models.FileField(upload_to=get_upload_path, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def remove_room(self):
        self.room = None
        self.save()
