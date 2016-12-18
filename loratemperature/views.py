from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import SensorData
import datetime


def index(request):
    return HttpResponse("I'm alive!!!")


def number_data(request, number_field):
    sensor_string = str(number_field)
    sd = SensorData(sensor_data=sensor_string + " Degrees Celcius", pub_date=datetime.datetime.now())
    sd.save()

    return HttpResponse("Number Data: %s" % number_field)


def string_data(request, string_field):
    # sd = SensorData(sensor_data=string_field,pub_date=time.time())
    # sd.save()
    return HttpResponse("String Data: %s" % string_field)

