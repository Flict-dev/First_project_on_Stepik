from django.contrib import admin

from .models import Departure, Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'description',
        'price',
        'duration',
        'country',
        'date',
        'stars'
    )
    list_display_links = ('name',)


@admin.register(Departure)
class DepartureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
        )
    list_display_links = ('name',)