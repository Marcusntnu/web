from django_hosts import host
from internal import urls as internal_urls
from web import settings

host_patterns = (
    host(r"(www|)", settings.ROOT_URLCONF, name="main"),
    host(r"(internal|internt)", internal_urls, name="internal"),
)
