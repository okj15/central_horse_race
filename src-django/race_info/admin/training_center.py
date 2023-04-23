from django.contrib import admin


class TrainingCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
