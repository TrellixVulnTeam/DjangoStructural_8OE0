from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('dbtemplate', views.dbtemplate),
    path('rcwall', views.rcwall)

]