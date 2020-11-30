from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def arduino(request):
    return render(request, 'core/arduino.html')

def circuitos_digitales(request):
    return render(request, 'core/circuitos_digitales.html')

def python(request):
    return render(request, 'core/python.html')

def raspberry(request):
    return render(request, 'core/raspberry.html')

def store(request):
    return render(request, 'core/store.html')




