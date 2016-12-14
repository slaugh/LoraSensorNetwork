from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("I'm alive!!!")


def number_data(request, number_field):
    return HttpResponse("Number Data: %s" % number_field)



