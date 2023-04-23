from django.contrib import admin

from race_info.models import TrackCondition


class TrackConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
