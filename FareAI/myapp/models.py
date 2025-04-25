from django.db import models

# Create your models here.
class Placeinfo(models.Model):
    place=models.CharField(max_length=255, blank=True, null=True ,  )
    latitude=models.FloatField(null=True, blank=True)
    longitude= models.FloatField(null=True, blank=True)


    