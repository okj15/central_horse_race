from django.contrib import admin

from race_info.models import TrackType


class TrackTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
