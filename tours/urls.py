from django.urls import path
from .views import MainView, DepatureView, TourView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('depature/<str:slug>/', DepatureView.as_view(), name='depature'),
    path('tour/<int:id>/', TourView.as_view(), name='tour_detail'),
]
