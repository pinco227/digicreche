# Generated by Django 3.2.6 on 2021-10-25 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20210910_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activities.activitytype'),
        ),
    ]
