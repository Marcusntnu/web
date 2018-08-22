from django.http import HttpResponse
from django.urls import path

from internal.url_util import require_internal

urlpatterns = require_internal([
    path("", lambda x: HttpResponse(x.user.username)),
    path("test", lambda x: HttpResponse("test")),
])
