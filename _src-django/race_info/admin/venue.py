from django.contrib import admin


class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
