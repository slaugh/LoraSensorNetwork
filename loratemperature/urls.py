from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<number_field>[0-9]+)/$', views.number_data, name='number_data'),
    url(r'^(?P<string_field>\w+)/$', views.string_data, name='string_data'),

]

