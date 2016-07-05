from django.contrib import admin

from applications.commands.models import Command


class CommandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Command, CommandAdmin)
