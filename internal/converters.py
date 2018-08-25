from internal.models import Member


class MemberSelect:
    regex = "[0-9]+"

    def to_python(self, value):
        Member.objects.get(pk=int(value))

    def to_url(self, value):
        return str(value.pk)
