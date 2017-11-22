# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-11-22 14:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('make_queue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotaSewing',
            fields=[
                ('quota_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='make_queue.Quota')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('make_queue.quota',),
        ),
        migrations.CreateModel(
            name='ReservationSewing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('event', models.BooleanField(default=False)),
                ('showed', models.NullBooleanField(default=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SewingMachine',
            fields=[
                ('machine_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='make_queue.Machine')),
            ],
            bases=('make_queue.machine',),
        ),
        migrations.AddField(
            model_name='reservationsewing',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='make_queue.Machine'),
        ),
        migrations.AddField(
            model_name='reservationsewing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
