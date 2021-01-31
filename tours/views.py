from django.shortcuts import render
from django.views.generic import View
from .models import Departure, Tour


class MainView(View):
    def get(self, request):
        tours = Tour.objects.reverse()[:6]
        departures = Departure.objects.all()
        context = {
            'title': 'Stepik Travel',
            'tours': tours,
            'departures': departures,
        }
        return render(
            request,
            'main_page/index.html',
            context=context
        )


class DepartureView(View):
    def get(self, request, slug):
        max_duration = 0
        min_duration = 30000
        max_price = 0
        min_price = 300000

        departures = Departure.objects.all()
        local_departure = Departure.objects.get(slug=slug)
        tours = Tour.objects.filter(departure=local_departure.id).order_by('name')
        count_tours = tours.count()
        for tour in tours:
            if tour.price < min_price:
                min_price = tour.price
            if tour.price > max_price:
                max_price = tour.price
            if tour.duration > max_duration:
                max_duration = tour.duration
            if tour.duration < min_duration:
                min_duration = tour.duration
        context = {
            'departures': departures,
            'tours': tours,
            'loc_dep': local_departure,
            'count_tours': count_tours,
            'min_duration': min_duration,
            'max_duration': max_duration,
            'min_price': min_price,
            'max_price': max_price,
        }
        return render(
            request,
            'departure/departure.html',
            context=context
        )


class TourView(View):
    def get(self, request, pk):
        tour = Tour.objects.get(id=pk)
        local_departure = Departure.objects.all()
        departures = Departure.objects.all()
        context = {
            'title': tour.name,
            'tour': tour,
            'local_departure': local_departure,
            'departures': departures,
            'tour_stars': range(tour.stars),

        }
        return render(
            request,
            'detail_tour/tour.html',
            context=context
        )
