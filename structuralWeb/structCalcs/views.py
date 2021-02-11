from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'structCalcs/index.html')


def dbtemplate(request):
    return render(request, 'structCalcs/dbtemplate.html')


def rcwall(request):
    return render(request, 'structCalcs/rcwall.html')


def padfooting(request):
    return render(request, 'structCalcs/padfooting.html')


def rcbeam(request):
    return render(request, 'structCalcs/rcbeam.html')


def rccolumn(request):
    return render(request, 'structCalcs/rccolumn.html')


def reinlaps(request):
    return render(request, 'structCalcs/reinlaps.html')


def retainingwall(request):
    return render(request, 'structCalcs/retainingwall.html')


def steelcalculator(request):
    return render(request, 'structCalcs/steelcalculator.html')
