from django.shortcuts import render
from django.views.generic import View
from .models import Depature, Tour


class MainView(View):
    def get(self, request):
        tours = Tour.objects.reverse()[:6]
        depatures = Depature.objects.all()
        context = {
            'title': 'Stepik Travel',
            'tours': tours,
            'depatures': depatures,
        }
        return render(
            request,
            'main_page/index.html',
            context=context
        )


class DepatureView(View):
    def get(self, request, slug):
        depatures = Depature.objects.all()
        local_depature = Depature.objects.get(slug=slug)
        tours = Tour.objects.filter(depature=local_depature.id).all()
        max_duration = 0
        min_duration = 3000
        max_price = 0
        min_price = 300000
        all_tors = 0
        for tour in tours:
            all_tors += 1
            if tour.price < min_price:
                min_price = tour.price
            elif tour.price > max_price:
                max_price = tour.price
            if tour.duration > max_duration:
                max_duration = tour.duration
            elif tour.duration < min_duration:
                min_duration = tour.duration
        context = {
            'depatures': depatures,
            'tours': tours,
            'loc_dep': local_depature,
            'all_tours': all_tors,
            'min_duration': min_duration,
            'max_duration': max_duration,
            'min_price': min_price,
            'max_price': max_price,
        }
        return render(
            request,
            'depature/depature.html',
            context=context
        )


class TourView(View):
    def get(self, request, id):
        tour = Tour.objects.get(id=id)
        local_depature = Depature.objects.all()
        depatures = Depature.objects.all()
        context = {
            'title': tour.name,
            'tour': tour,
            'local_depature': local_depature,
            'depatures': depatures,
            'tour_stars': range(tour.stars),

        }
        return render(
            request,
            'detail_tour/tour.html',
            context=context
        )
