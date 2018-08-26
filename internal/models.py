from django.contrib.auth.models import User, Group
from django.db import models

from groups.models import Committee


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
            ("can_register_new_member", "Can register new member"),
            ("can_edit_group_membership", "Can edit the groups a member is part of, including (de)activation")
        )

    def __str__(self):
        return self.user.get_full_name() + " - " + ["Inaktive", "Aktiv"][self.active]

    def properties_status(self):
        return (sum(prop.value for prop in self.memberproperty_set.all()) / len(MemberProperty.name_choices)) * 100

    def get_name(self):
        if self.user is not None:
            return self.user.get_full_name()
        return self.memberinactive.full_name

    def get_committee(self):
        user_committees = self.user.groups.all() if self.user is not None else self.memberinactive.groups.all()
        committees = Committee.objects.filter(group__in=user_committees).all()

        if len(committees) == 1:
            return committees[0].name + (" - " + self.role) * (len(self.role) != 0)

        # Members of more than one committee are managers (leder) and deputies (nestleder) in their respective committee
        for committee in committees:
            name = committee.name
            if name == "Styret":
                continue

            return name + " - " + self.role

        return ""

    def toggle_active(self):
        if self.active:
            # If the user is active, create a dummy user (with a random password) to keep the data of the inactive user
            # as to be able to remove the permissions for the user, while still keeping history of inactive members
            # for possible reactivation of their membership and general bookkeeping.

            inactive_data = MemberInactive.objects.create(username=self.user.username,
                                                          full_name=self.user.get_full_name(), member=self)
            for group in self.user.groups.all():
                inactive_data.groups.add(group)
                group.user_set.remove(self.user)

            self.user = None
        else:
            users = User.objects.filter(username=self.memberinactive.username)

            # Older members do not have an account on the website, and can therefore not be activated
            if not users.exists():
                return

            self.user = users.first()

            for group in self.memberinactive.groups.all():
                group.user_set.add(self.user)

            self.memberinactive.delete()

        self.active = not self.active

        self.save()


class MemberInactive(models.Model):
    groups = models.ManyToManyField(Group)
    username = models.fields.CharField(max_length=256)
    full_name = models.fields.CharField(max_length=256)
    member = models.OneToOneField(Member, on_delete=models.DO_NOTHING, null=True, blank=True)


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
