from django.db import models

class Transmission(models.Model):
    timestamp = models.DateTimeField()
    country_code_from = models.CharField(max_length=20)
    country_code_to = models.CharField(max_length=20)
    capacity = models.FloatField()

