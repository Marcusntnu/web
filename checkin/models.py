from datetime import time

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Skill(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Ferdighet")

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    card_id = models.CharField(max_length=100, verbose_name="Kortnummer")
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name="Profilbilde")
    on_make = models.BooleanField(default=False, verbose_name="Innsjekkingsstatus")

    def __str__(self):
        return self.card_id


class UserSkill(models.Model):
    level_choices = (
        (1, "nybegynner"),
        (2, "viderekommen"),
        (3, "ekspert"),
    )
    skill = models.ForeignKey(Skill, null=True, on_delete=models.SET_NULL)
    skill_level = models.IntegerField(choices=level_choices)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.skill_level)