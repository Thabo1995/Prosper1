# Generated by Django 3.2.3 on 2021-08-04 11:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_party_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingevent',
            name='closing_date_of_event_registration',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votingevent',
            name='date_of_event_registration',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
