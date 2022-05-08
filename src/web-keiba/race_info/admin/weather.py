from django.contrib import admin

from race_info.models import Weather


class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
