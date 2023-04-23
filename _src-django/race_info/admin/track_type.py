from django.contrib import admin


class TrackTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
