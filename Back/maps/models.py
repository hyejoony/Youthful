from django.db import models
from django.conf import settings

# Create your models here.
class Map(models.Model):
    road_address_name = models.TextField()
    distance = models.TextField()
    phone = models.TextField()
    place_name = models.TextField()
    place_url = models.TextField()
    x = models.TextField()
    y = models.TextField()








