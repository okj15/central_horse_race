from django.contrib import admin


class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
