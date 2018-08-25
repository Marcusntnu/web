from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    email = models.fields.EmailField(null=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True)
    role = models.fields.CharField(max_length=32)
    phone_number = models.fields.CharField(max_length=32)
    study_program = models.CharField(max_length=32)
    card_number = models.CharField(max_length=32)
    active = models.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def create(cls, *args, **kwargs):
        member = cls(*args, **kwargs)
        member.save()
        for (property_name, _) in MemberProperty.name_choices:
            MemberProperty.objects.create(name=property_name, value=property_name == "Nettside", member=member)
        return member

    class Meta:
        permissions = (
            ("is_internal", "Is a member of MAKE NTNU"),
        )

    def __str__(self):
        return self.user.get_full_name() + " - " + ["Inaktive", "Aktiv"][self.active]

    def properties_status(self):
        return (sum(prop.value for prop in self.memberproperty_set.all())/len(MemberProperty.name_choices))*100


class MemberProperty(models.Model):
    name_choices = (
        ("Drive", "Drive"),
        ("Slack", "Slack"),
        ("Kalender", "Kalender"),
        ("Trello", "Trello"),
        ("E-postlister", "E-postlister"),
        ("Nettside", "Nettside")
    )

    name = models.fields.CharField(max_length=32, choices=name_choices)
    value = models.fields.BooleanField()
    member = models.ForeignKey(Member, models.CASCADE)
