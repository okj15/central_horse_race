from django.contrib import admin

from race_info.models import Gender


class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
