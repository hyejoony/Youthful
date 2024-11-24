from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserManager(BaseUserManager):
    """이메일을 고유 식별자로 사용하는 커스텀 유저 매니저"""

    def create_user(self, email, password=None, **extra_fields):
        """주어진 이메일과 비밀번호로 일반 유저 생성"""
        if not email:
            raise ValueError('이메일은 필수입니다.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """주어진 이메일과 비밀번호로 관리자 유저 생성"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    INCOME_CHOICES = [
        ('0~50%', '약 100만원'),
        ('51~75%', '약 150만원'),
        ('76~100%', '약 200만원'),
        ('101~200%', '약 450만원'),
        ('200%~', '약 450초과'),
    ]

    # 직업 선택 옵션
    CAREER_CHOICES = [
        ('학생', 'student'),
        ('회사원', 'office_worker'),
        ('공무원', 'public_servant'),
        ('전문직', 'professional'),
        ('자영업자', 'self_employed'),
        ('프리랜서', 'freelancer'),
        ('사업자', 'business_owner'),
        ('아르바이트/비정규직', 'part_time'),
        ('전업주부', 'housewife'),
        ('무직/구직중', 'unemployed'),
        ('은퇴자', 'retired'),
        ('농업/어업/임업', 'farmer'),
        ('군인', 'soldier'),
        ('교사/교육자', 'teacher'),
        ('의료종사자', 'medical'),
        ('금융업 종사자', 'financial'),
        ('IT업계 종사자', 'it_worker'),
        ('서비스업 종사자', 'service_industry'),
        ('제조업 종사자', 'manufacturing'),
        ('스타트업 창업자', 'startup_founder'),
        ('사회복지사', 'social_worker'),
        ('연구원', 'researcher'),
        ('기타', 'other'),
    ]

    # 지역 선택 옵션
    REGION_CHOICES = [
        ('서울특별시', 'seoul'),
        ('부산광역시', 'busan'),
        ('대구광역시', 'daegu'), 
        ('인천광역시', 'incheon'),
        ('광주광역시', 'gwangju'),
        ('대전광역시', 'daejeon'),
        ('울산광역시', 'ulsan'),
        ('세종특별자치시', 'sejong'),
        ('경기도', 'gyeonggi'),
        ('강원특별자치도', 'gangwon'),
        ('충청북도', 'chungbuk'),
        ('충청남도', 'chungnam'),
        ('전라북도', 'jeonbuk'),
        ('전라남도', 'jeonnam'),
        ('경상북도', 'gyeongbuk'),
        ('경상남도', 'gyeongnam'),
        ('제주특별자치도', 'jeju'),
    ]

    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=100, blank=True)
    birthyear = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(9999)]
    )
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    income = models.CharField(max_length=20, choices=INCOME_CHOICES)
    career = models.CharField(max_length=20, choices=CAREER_CHOICES)
    region = models.CharField(max_length=10, choices=REGION_CHOICES)
    condition1 = models.BooleanField(default=False)
    condition2 = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birthyear', 'income', 'career', 'region', 'condition1', 'condition2'] #필수 필드 넣기

    def __str__(self):
        return self.email