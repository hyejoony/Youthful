from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()

# 소득 수준 선택 옵션
INCOME_CHOICES = [
    ('0-50%', '약 100만원'),
    ('51~75%', '약 150만원'),
    ('76~100%', '약 200만원'),
    ('101~200%', '약 450만원'),
    ('200%~', '약 450만원 초과'),
]

# 직업 선택 옵션
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

# 지역 선택 옵션
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


class CustomRegisterSerializer(RegisterSerializer):
    """
    커스텀 회원가입 시리얼라이저
    기본 회원가입 필드 외에 추가 정보를 포함
    """
    birthyear = serializers.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(9999)]
    )
    profile_img = serializers.ImageField(required=False, allow_null=True)
    income = serializers.ChoiceField(choices=INCOME_CHOICES)
    career = serializers.ChoiceField(choices=CAREER_CHOICES)
    region = serializers.ChoiceField(choices=REGION_CHOICES)
    condition1 = serializers.BooleanField(default=False)
    condition2 = serializers.BooleanField(default=False)

    def get_cleaned_data(self):
        """
        기본 cleaned_data에 추가 필드 정보를 포함하여 반환
        """
        data = super().get_cleaned_data()
        data.update({
            'birthyear': self.validated_data.get('birthyear', ''),
            'profile_img': self.validated_data.get('profile_img', ''),
            'income': self.validated_data.get('income', ''),
            'career': self.validated_data.get('career', ''),
            'region': self.validated_data.get('region', ''),
            'condition1': self.validated_data.get('condition1', False),
            'condition2': self.validated_data.get('condition2', False),
        })
        return data


class CustomUserDetailsSerializer(UserDetailsSerializer):
    """
    커스텀 사용자 상세 정보 시리얼라이저
    기본 사용자 정보 외에 추가 필드 포함
    """
    birthyear = serializers.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(9999)]
    )
    profile_img = serializers.ImageField(required=False, allow_null=True)
    income = serializers.ChoiceField(choices=INCOME_CHOICES)
    career = serializers.ChoiceField(choices=CAREER_CHOICES)
    region = serializers.ChoiceField(choices=REGION_CHOICES)
    condition1 = serializers.BooleanField()
    condition2 = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 
                  'birthyear', 'profile_img', 'income', 'career', 'region', 
                  'condition1', 'condition2')
        read_only_fields = ('email',)

    def update(self, instance, validated_data):
        """
        사용자 정보 업데이트 시 프로필 이미지 처리
        """
        # 프로필 이미지 업데이트 시 기존 이미지 삭제
        if 'profile_img' in validated_data and instance.profile_img:
            instance.profile_img.delete()

        return super().update(instance, validated_data)