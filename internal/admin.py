from django.contrib import admin

# Register your models here.
from internal.models import Member, MemberProperty

admin.site.register(Member)
admin.site.register(MemberProperty)
