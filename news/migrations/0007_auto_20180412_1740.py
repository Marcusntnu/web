# Generated by Django 2.0.4 on 2018-04-12 15:40

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180405_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Publishing date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Publishing time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='multiday',
            field=models.BooleanField(default=False, verbose_name='One registration'),
        ),
        migrations.AlterField(
            model_name='newsbase',
            name='contain',
            field=models.BooleanField(default=False, verbose_name="Don't crop the image"),
        ),
        migrations.AlterField(
            model_name='newsbase',
            name='featured',
            field=models.BooleanField(default=True, verbose_name='Highlighted'),
        ),
        migrations.AlterField(
            model_name='newsbase',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Hidden'),
        ),
        migrations.AlterField(
            model_name='newsbase',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='newsbase',
            name='private',
            field=models.BooleanField(default=False, verbose_name='MAKE internal'),
        ),
        migrations.AlterField(
            model_name='newsbase',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='hidden',
            field=models.BooleanField(default=True, verbose_name='Hidden'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='place',
            field=models.CharField(blank=True, max_length=100, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='place_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='Location URL'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Publishing date'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='pub_time',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Publishing time'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='start_time',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Start time'),
        ),
    ]
