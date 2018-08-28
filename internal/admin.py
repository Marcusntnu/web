from django.contrib import admin

# Register your models here.
from internal.models import Member, MemberProperty, Secret, SecretFavorite

admin.site.register(Member)
admin.site.register(MemberProperty)
admin.site.register(Secret)
admin.site.register(SecretFavorite)
