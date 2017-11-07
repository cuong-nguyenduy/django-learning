from django.contrib import admin
from . import models


class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember


# Register your models here.
admin.site.register(models.Group)
# admin.site.register(models.GroupMember)
