from django.contrib import admin

from race_info.models import Direction


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
