from django.contrib import admin


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
