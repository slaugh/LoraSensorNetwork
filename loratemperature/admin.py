from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import SensorData


class SensorDataAdmin(admin.ModelAdmin):
    fields = ['sensor_data','pub_date']

    list_display = ('sensor_data','__str__','pub_date')


admin.site.register(SensorData, SensorDataAdmin)