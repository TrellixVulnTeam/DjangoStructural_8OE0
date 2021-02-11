from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dbtemplate', views.dbtemplate),
    path('rcwall', views.rcwall, name='rcwall'),
    path('padfooting', views.padfooting, name='padfooting'),
    path('rcbeam', views.rcbeam, name='rcbeam'),
    path('rccolumn', views.rccolumn, name='rccolumn'),
    path('reinlaps', views.reinlaps, name='reinlaps'),
    path('retainingwall', views.retainingwall, name='retainingwall'),
    path('steelcalculator', views.steelcalculator, name='steelcalculator'),
]
