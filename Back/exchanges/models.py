from django.db import models
from django.conf import settings

# Create your models here.
class Exchange(models.Model):
    country_name= models.CharField(max_length=10) 
    cur_unit = models.CharField(max_length=20)
    link = models.TextField()
    basic_rate = models.TextField()
    cash_send = models.TextField()
    cash_receive = models.TextField()
    image_src = models.TextField()







