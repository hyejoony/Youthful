from django.db import models
from django.conf import settings


# Create your models here.
class Subsidy(models.Model):
    like_users = models.ManyToManyField(            # 찜
        settings.AUTH_USER_MODEL, related_name='like_subsidies'
    )
    name = models.CharField(max_length=20)          # 서비스 명
    name_category = models.CharField(max_length=5)  # 서비스 명 카테고리화
    target = models.TextField()                     # 지원 대상
    content = models.TextField()                    # 지원 내용
    contact = models.CharField(max_length=20)       # 문의처


class SubsidyComment(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subsidy_comments'
    )
    subsidy = models.ForeignKey(
        Subsidy, on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField()
    rating = models.CharField(max_length=10, choices=RATING_CHOICES)   # 별점
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





