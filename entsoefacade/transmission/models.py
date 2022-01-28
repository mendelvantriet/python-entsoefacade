from django.db import models
from django.db.models.constraints import UniqueConstraint


class Transmission(models.Model):
    timestamp = models.DateTimeField()
    country_code_from = models.CharField(max_length=20)
    country_code_to = models.CharField(max_length=20)
    capacity = models.FloatField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=('timestamp', 'country_code_from', 'country_code_to'), name='constraint_unique'),
        ]
