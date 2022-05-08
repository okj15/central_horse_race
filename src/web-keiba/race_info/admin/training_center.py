from django.contrib import admin

from race_info.models import TrainingCenter


class TrainingCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
