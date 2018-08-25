from django_hosts import host
from web import settings

host_patterns = (
    host(r"(www|)", settings.ROOT_URLCONF, name="main"),
    host(r"(internal|internt)", "internal.urls", name="internal"),
)