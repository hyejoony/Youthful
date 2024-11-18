from django.db import models
from django.conf import settings

# Create your models here.
class Exchange(models.Model):
    cur_unit = models.CharField(max_length=20)
    basic_rate = models.IntegerField()
    remittance_send = models.IntegerField()
    remittance_receive = models.IntegerField()







