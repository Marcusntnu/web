# Generated by Django 2.0 on 2018-08-24 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Drive', 'Drive'), ('Slack', 'Slack'), ('Kalender', 'Kalender'), ('Trello', 'Trello'), ('E-postlister', 'E-postlister'), ('Nettside', 'Nettside')], max_length=32)),
                ('value', models.BooleanField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internal.Member')),
            ],
        ),
    ]
