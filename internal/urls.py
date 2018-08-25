from django.http import HttpResponse
from django.urls import path

from internal.url_util import require_internal
from internal.views import *

urlpatterns = require_internal([
    path("", HomePageView.as_view(), name="home"),
    path("members", MemberListView.as_view(), name="members"),
    path("members/new", NewMemberView.as_view(), name="new_member")
])
