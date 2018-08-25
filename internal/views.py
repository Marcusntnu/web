from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

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
        context.update({
            "users": User.objects.all().filter(member__isnull=True),
            "committees": Committee.objects.all()
        })
        return context

    def post(self, request):
        user = request.POST.get("user", None)
        committee = request.POST.get("committee", None)

        print(user, committee)

        if user is None or committee is None or not user.isdigit() or not committee.isdigit():
            return self.get(request)

        user = User.objects.filter(member__isnull=True).get(pk=int(user))
        group = Committee.objects.get(pk=int(committee)).group

        if user is None or group is None:
            return self.get(request)

        group.user_set.add(user)
        Member.create(user=user, active=True, email=user.email)

        return redirect(reverse("members"))


class HomePageView(TemplateView):
    template_name = "internal/main.html"
