# Generated by Django 3.2.6 on 2021-10-16 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0008_2_5'),
        ('accounts', '0011_digicrecheuser_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='digicrecheuser',
            name='customer',
            field=models.ForeignKey(blank=True, help_text="The user's Stripe Customer object, if it exists", null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.customer'),
        ),
    ]