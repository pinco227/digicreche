# Generated by Django 3.2.6 on 2021-10-22 12:56

from django.conf import settings
from django.db import migrations, models
import pupils.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pupils', '0003_alter_pupil_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='children', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=pupils.models.get_upload_path),
        ),
    ]