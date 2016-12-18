from django.db import models

# Use the following command to generate the SQL:
# python manage.py sqlmigrate loratemperature 0001

# Create your models here.
from django.db import models


class SensorData(models.Model):
    sensor_data = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "Produced By Scott Laughlin - Data Collected using Long Range wireless (LoRa)"