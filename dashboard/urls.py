from django.urls import path
from .views import dashboard_stats, dashboard_chart_data

urlpatterns = [
    path('stats/', dashboard_stats, name='dashboard_stats'),
    path('chart-data/', dashboard_chart_data, name='dashboard_chart_data'),
]
