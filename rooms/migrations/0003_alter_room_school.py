# Generated by Django 3.2.6 on 2021-09-06 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_alter_school_manager'),
        ('rooms', '0002_remove_room_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='schools.school'),
        ),
    ]
