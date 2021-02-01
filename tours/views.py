from django.db.models import Max, Min
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
        departures = Departure.objects.all()
        local_departure = Departure.objects.get(slug=slug)
        tours = Tour.objects.filter(departure=local_departure.id).order_by('name')
        count_tours = tours.count()
        max_price = Tour.objects.filter(departure=local_departure.id).\
            aggregate(m_price=Max('price'))['m_price']
        min_price = Tour.objects.filter(departure=local_departure.id).\
            aggregate(m_price=Min('price'))['m_price']
        max_duration = Tour.objects.filter(departure=local_departure.id).\
            aggregate(duration=Max('duration'))['duration']
        min_duration = Tour.objects.filter(departure=local_departure.id).\
            aggregate(duration=Min('duration'))['duration']

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
