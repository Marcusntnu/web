# Generated by Django 2.0.5 on 2018-05-02 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20180501_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Publishing date'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='pub_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Publishing date'),
        ),
        migrations.AlterField(
            model_name='timeplace',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Start date'),
        ),
    ]