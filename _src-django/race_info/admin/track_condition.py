from django.contrib import admin


class TrackConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
