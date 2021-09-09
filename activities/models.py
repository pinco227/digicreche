from django.db import models
from django.utils.text import slugify
from pupils.models import Pupil
import os


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
        verbose_name_plural = "Activities"

    def __str__(self):
        return (self.pupil.first_name + ' ' +
                self.pupil.last_name + ' > ' +
                self.type.name + ' > ' +
                self.created_at.strftime("%d/%m/%y %H:%M"))


class ActivityImage(models.Model):
    """ CREDIT:
    https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/
    """
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE,
                                 related_name='images')
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return (self.activity.pupil.first_name + ' ' +
                self.activity.pupil.last_name)

    def get_upload_path(instance, filename):
        pupil = instance.activity.pupil
        pupil_slug = slugify(pupil.first_name + ' ' + pupil.last_name)
        return os.path.join(
            pupil.school.slug,
            pupil.room.name,
            pupil_slug,
            instance.activity.created_at.date().strftime("%d-%m-%y"),
            filename)
