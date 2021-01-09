from django.contrib import admin

from .models import Depature, Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'price', 'duration', 'country', 'date', 'stars')
    list_display_links = ('name',)


@admin.register(Depature)
class DepatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

