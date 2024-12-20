from django.contrib import admin
from django.urls import path
from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/pie/', PieCountbySeverity, name='pie-chart'),  # Ensure proper path here
    path('chart/line/', LineCountbyMonth, name='line-chart'),
    path('chart/multiline/', MultilineIncidentTop3Country, name='multiline-chart'),
    path('chart/bar/', multipleBarbySeverity, name='bar-chart'),
    path('chart.html', views.chart_view, name='chart-html'),  # This should be defined
    path('map-station/', views.map_station, name='map-station'),
    path('map-incident/', views.map_incident, name='map-incident'),
    path('stations/', views.stations_view, name='stations'),
]

    
