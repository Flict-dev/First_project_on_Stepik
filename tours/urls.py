from django.urls import path
from .views import MainView, DepartureView, TourView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('departure/<str:slug>/', DepartureView.as_view(), name='departure'),
    path('tour/<int:pk>/', TourView.as_view(), name='tour_detail'),
]
