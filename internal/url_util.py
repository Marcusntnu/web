from django.contrib.auth.decorators import permission_required
from django.urls import URLPattern, URLResolver, include, path
from django_hosts import reverse


class DecoratedURLPattern(URLPattern):
    def resolve(self, *args, **kwargs):
        result = super(DecoratedURLPattern, self).resolve(*args, **kwargs)
        if result:
            result.func = self._decorate_with(result.func)
        return result


class DecoratedURLResolver(URLResolver):
    def resolve(self, *args, **kwargs):
        result = super(DecoratedURLResolver, self).resolve(*args, **kwargs)
        if result:
            result.func = self._decorate_with(result.func)
        return result


def decorated_includes(func, includes, *args, **kwargs):
    urlconf_module, app_name, namespace = includes
    patterns = getattr(urlconf_module, 'urlpatterns', urlconf_module)
    for item in patterns:
        if isinstance(item, URLPattern):
            item.__class__ = DecoratedURLPattern
            item._decorate_with = func

        elif isinstance(item, URLResolver):
            item.__class__ = DecoratedURLResolver
            item._decorate_with = func

    return urlconf_module, app_name, namespace


def require_internal(pattern_list):
    return [
        path("", decorated_includes(
            permission_required("internal.is_internal", login_url=reverse("login", host="main", host_args=["www"])),
            include(pattern_list)
        ))
    ]
