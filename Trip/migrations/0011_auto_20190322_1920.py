# Generated by Django 2.1.7 on 2019-03-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0010_auto_20190322_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='post date'),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='trip_date',
            field=models.DateTimeField(default=None, verbose_name='Trip date'),
        ),
    ]