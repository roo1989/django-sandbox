from django.db import models

class ScraperRealtor(models.Model):
    source = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    type = models.CharField(max_length=250)
    size = models.IntegerField()
    built = models.BigIntegerField()
    rooms = models.IntegerField()
    garage = models.BooleanField()
    description = models.TextField()
