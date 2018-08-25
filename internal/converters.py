from internal.models import Member


class MemberSelect:
    regex = "[0-9]+"

    def to_python(self, value):
        return Member.objects.get(pk=int(value))

    def to_url(self, value):
        return str(value.pk)
