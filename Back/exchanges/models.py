from django.db import models
from django.conf import settings

# Create your models here.
class Exchange(models.Model):
    cur_unit = models.CharField(max_length=20)
    link = models.TextField()
    basic_rate = models.TextField()
    remittance_send = models.TextField()
    remittance_receive = models.TextField()
    image_src = models.TextField()







