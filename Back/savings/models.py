from django.db import models
from django.conf import settings

# Create your models here.
class SavingProduct(models.Model):
    like_users = models.ManyToManyField(    # 찜
        settings.AUTH_USER_MODEL, related_name='like_savings'
    )
    dcls_month = models.TextField()         # 공시 제출월
    kor_co_nm = models.TextField()          # 금융 회사명
    fin_prdt_nm = models.TextField()        # 금융상품명
    join_way = models.TextField()           # 가입 방법
    mtrt_int = models.TextField()           # 만기 후 이자율
    spcl_cnd = models.TextField()           # 우대조건
    join_deny = models.IntegerField()       # 가입 제한
    join_member = models.TextField()        # 가입 대상
    etc_note = models.TextField()           # 기타 유의사항
    max_limit = models.IntegerField()       # 최고한도
    fin_prdt_cd = models.TextField()        # 금융상품 코드

class SavingOption(models.Model):
    saving_product = models.ForeignKey(
        SavingProduct, on_delete=models.CASCADE
    )
    intr_rate_type_nm = models.TextField()  # 저축 금리 유형명 
    rsrv_type_nm = models.TextField()       # 적립 유형명
    save_trm = models.IntegerField()        # 저축 기간(단위: 개월)
    intr_rate = models.DecimalField(        # 저축 금리(소수점 2자리)
        max_digits=None, max_length=2
    )      
    intr_rate2 = models.DecimalField(       # 저축 우대금리(소수점 2자리)
        max_digits=None, max_length=2
    )   