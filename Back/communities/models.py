from django.db import models
from django.conf import settings

# Create your models here.
class Community(models.Model):
    KEYWORD_CHOICES = [
        ('saving', '적금'),
        ('deposit', '예금'),
        ('subsidy', '지원금'),
        ('etc', '기타'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='communities'
    )
    title = models.CharField(max_length=50)
    keyword = models.CharField(max_length=10, choices=KEYWORD_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CommunityComment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='community_comments'
    )
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


