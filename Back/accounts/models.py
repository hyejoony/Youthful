from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class User(AbstractUser):
    INCOME_CHOICES = [
        ('0-50%', '약 100만원'),
        ('51~75%', '약 150만원'),
        ('76~100%', '약 200만원'),
        ('101~200%', '약 450만원'),
        ('200%~', '약 450초과'),
    ]

    CAREER_CHOICES = [
        ('student', '학생'),
        ('office_worker', '회사원'),
        ('public_servant', '공무원'),
        ('professional', '전문직'),
        ('self_employed', '자영업자'),
        ('freelancer', '프리랜서'),
        ('business_owner', '사업자'),
        ('part_time', '아르바이트/비정규직'),
        ('housewife', '전업주부'),
        ('unemployed', '무직/구직중'),
        ('retired', '은퇴자'),
        ('farmer', '농업/어업/임업'),
        ('soldier', '군인'),
        ('teacher', '교사/교육자'),
        ('medical', '의료종사자'),
        ('financial', '금융업 종사자'),
        ('it_worker', 'IT업계 종사자'),
        ('service_industry', '서비스업 종사자'),
        ('manufacturing', '제조업 종사자'),
        ('startup_founder', '스타트업 창업자'),
        ('social_worker', '사회복지사'),
        ('researcher', '연구원'),
        ('other', '기타'),
    ]

    REGION_CHOICES = [
        ('seoul', '서울특별시'),
        ('busan', '부산광역시'),
        ('daegu', '대구광역시'),
        ('incheon', '인천광역시'),
        ('gwangju', '광주광역시'),
        ('daejeon', '대전광역시'),
        ('ulsan', '울산광역시'),
        ('sejong', '세종특별자치시'),
        ('gyeonggi', '경기도'),
        ('gangwon', '강원특별자치도'),
        ('chungbuk', '충청북도'),
        ('chungnam', '충청남도'),
        ('jeonbuk', '전라북도'),
        ('jeonnam', '전라남도'),
        ('gyeongbuk', '경상북도'),
        ('gyeongnam', '경상남도'),
        ('jeju', '제주특별자치도'),
    ]

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    birthyear = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(9999)]
    )
    profile_img = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    income = models.CharField(max_length=20, choices=INCOME_CHOICES)
    career = models.CharField(max_length=20, choices=CAREER_CHOICES, blank=True)
    region = models.CharField(max_length=10, choices=REGION_CHOICES)
    condition1 = models.BooleanField(default=False)
    condition2 = models.BooleanField(default=False)

    def __str__(self):
        return self.username