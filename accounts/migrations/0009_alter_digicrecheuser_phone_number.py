# Generated by Django 3.2.6 on 2021-08-14 05:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_digicrecheuser_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digicrecheuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
