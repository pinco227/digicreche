# Generated by Django 3.2.6 on 2021-09-06 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0003_alter_room_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='teacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room', to=settings.AUTH_USER_MODEL),
        ),
    ]
