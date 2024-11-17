from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    like_users = models.ManyToManyField(        # 찜
        settings.AUTH_USER_MODEL, related_name='like_articles'
    )
    title = models.CharField(max_length=30)
    originallink = models.TextField()
    description = models.TextField()
    pubdate  = models.TextField()