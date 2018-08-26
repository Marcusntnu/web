from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from groups.models import Committee
from internal.models import Member


class MemberListView(TemplateView):
    template_name = "internal/members/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "members": Member.objects.all()
        })
        return context


class NewMemberView(TemplateView):
    template_name = "internal/members/register_member.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inactive_usernames = [member.memberinactive.username for member in Member.objects.filter(active=False).all()]
        context.update({
            "users": User.objects.all().filter(member__isnull=True).exclude(username__in=inactive_usernames),
            "committees": Committee.objects.all()
        })
        return context

    def post(self, request):
        user = request.POST.get("user", None)
        committee = request.POST.get("committee", None)

        if user is None or committee is None or not user.isdigit() or not committee.isdigit():
            return self.get(request)

        user = User.objects.filter(member__isnull=True).get(pk=int(user))
        group = Committee.objects.get(pk=int(committee)).group

        if user is None or group is None:
            return self.get(request)

        group.user_set.add(user)
        Member.create(user=user, active=True, email=user.email)

        return redirect(reverse("members"))


class ChangeMemberView(TemplateView):
    template_name = "internal/members/change_member.html"

    def get_context_data(self, member, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "member": member,
            "committees": Committee.objects.all(),
            "user_committees": Committee.objects.filter(group__in=member.user.groups.all()).all()
        })
        return context

    """
    Handling of form submit. Could perhaps use a form view, however most of it is custom adding and removal of groups
    """
    def post(self, request, member):
        has_permission = request.user.has_perm("internal.can_edit_group_membership")

        if member.user != request.user and not has_permission:
            return self.get(request, member)

        if has_permission:
            user_committees = list(Committee.objects.filter(group__in=member.user.groups.all()).all())
            selected_committees = Committee.objects.filter(pk__in=map(int, request.POST.getlist("committees"))).all()

            for committee in selected_committees:
                if committee in user_committees:
                    user_committees.remove(committee)
                else:
                    committee.group.user_set.add(member.user)

            # Remove the user from the groups that were not selected
            for not_found_committee in user_committees:
                not_found_committee.group.user_set.remove(member.user)

            member.role = request.POST.get("role")

        internal_systems = request.POST.getlist("system")
        for system in member.memberproperty_set.all():
            # Add and remove systems
            if (system.name in internal_systems and not system.value) or (
                    system.name not in internal_systems and system.value):
                system.value = not system.value
                system.save()

        member.email = request.POST.get("email")
        member.study_program = request.POST.get("study_program")
        member.phone_number = request.POST.get("phone_number")
        member.card_number = request.POST.get("card_number")

        member.save()

        return redirect(reverse("members"))


class HomePageView(TemplateView):
    template_name = "internal/main.html"


def handle_activation(request, member):
    if request.method == "POST" and (
            request.user == member.user or request.user.has_perm("internal.can_register_new_member")):
        member.toggle_active()

    return redirect(reverse("members"))
