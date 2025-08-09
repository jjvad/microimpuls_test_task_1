from django.urls import path
from .views import PressureRecordCreateView, LastRecordView, StatsView

urlpatterns = [
    path('api/create/', PressureRecordCreateView.as_view(), name='pressure-create'),
    path('api/last/', LastRecordView.as_view(), name='last-pressure'),
    path('api/stats/<str:period>/', StatsView.as_view(), name='pressure-stats'),
]