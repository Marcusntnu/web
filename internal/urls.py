from django.contrib.auth.decorators import permission_required
from django.urls import path, register_converter

from internal import converters
from internal.url_util import require_internal
from internal.views import *

register_converter(converters.MemberSelect, "member")

urlpatterns = require_internal([
    path("", HomePageView.as_view(), name="home"),
    path("members", MemberListView.as_view(), name="members"),
    path("members/new", permission_required("internal.can_register_new_member")(NewMemberView.as_view()), name="new_member"),
    path("members/<member:member>", ChangeMemberView.as_view(), name="change_member"),
    path("members/activate/<member:member>", handle_activation, name="activation_member"),
    path("secrets", SecretsView.as_view(), name="secrets"),
])
