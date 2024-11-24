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
<<<<<<< HEAD
    path('stations/', views.map_station, name='map-station'), 
    
=======
    path('stations', views.map_station, name='map-station'), 
>>>>>>> c654a48888151611e023a084f65f8b9916487702
]

    
