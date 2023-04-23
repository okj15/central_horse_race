from django.contrib import admin

from race_info.models import Venue


class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
