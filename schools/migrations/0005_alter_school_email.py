# Generated by Django 3.2.6 on 2021-10-19 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_school_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
