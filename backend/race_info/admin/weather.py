from django.contrib import admin


class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
