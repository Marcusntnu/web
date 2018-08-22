from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):

    email = models.fields.EmailField
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.fields.CharField(max_length=32)
    phone_number = models.fields.IntegerField
    study_program = models.CharField(max_length=32)
    card_number = models.CharField(max_length=32)
    active = models.BooleanField

    class Meta:
        permissions = (
            ("is_internal", "Is a member of MAKE NTNU"),
        )
