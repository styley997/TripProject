# Generated by Django 2.1.7 on 2019-03-22 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0014_auto_20190322_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evidence',
            name='trip',
        ),
        migrations.AddField(
            model_name='evidence',
            name='TripDetail',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Trip.TripDetail'),
        ),
    ]
