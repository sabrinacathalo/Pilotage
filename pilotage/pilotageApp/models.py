from django.db import models


class DataPilotage(models.Model):
    temperature = models.FloatField()
    date_time = models.DateTimeField('date published')
    # lumiere=models.FloatField(default=None)
    distance_obstacle=models.FloatField()
    distance_altitude=models.FloatField()
    humidite=models.FloatField()


