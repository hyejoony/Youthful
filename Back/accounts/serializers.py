from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from .models import User
import re

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


# 회원가입을 위한 시리얼라이즈
class CustomRegisterSerializer(RegisterSerializer):
    # 생년 필드: 1900년 이상 9999년 이하의 정수만 허용
    birthyear = serializers.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(9999)],
    )
    
    # 프로필 이미지 필드: 선택 사항으로 null 허용
    profile_img = serializers.ImageField(required=False, allow_null=True)
    
    # 소득, 경력, 지역 필드: 선택 가능한 값들 정의
    income = serializers.ChoiceField(choices=INCOME_CHOICES)
    career = serializers.ChoiceField(choices=CAREER_CHOICES)
    region = serializers.ChoiceField(choices=REGION_CHOICES)
    
    # 약관 동의 필드: 기본값은 False
    condition1 = serializers.BooleanField(default=False)
    condition2 = serializers.BooleanField(default=False)

    def validate_username(self, value):
        """
        아이디 유효성 검사: 영어 대소문자와 숫자만 허용, 최소 4자에서 최대 20자까지.
        """
        if not re.match(r'^[a-zA-Z0-9]{4,20}$', value):
            raise serializers.ValidationError('아이디는 영어 대소문자와 숫자로만 이루어져야 하며, 최소 4자에서 최대 20자여야 합니다.')
        return value

    def validate_email(self, value):
        """
        이메일 유효성 검사: 올바른 이메일 형식인지 확인.
        """
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise serializers.ValidationError('유효한 이메일 주소가 아닙니다.')
        return value

    def validate_password1(self, value):
        """
        비밀번호 유효성 검사: 최소 8자 이상, 최대 20자 이하,
        영문 대소문자, 숫자, 특수문자 중 2가지 이상 포함해야 함.
        """
        if len(value) < 8:
            raise serializers.ValidationError('비밀번호는 최소 8자 이상이어야 합니다.')
        if len(value) > 20:
            raise serializers.ValidationError('비밀번호는 최대 20자 이하여야 합니다.')
        
        # 비밀번호의 복잡성을 체크하기 위한 조건 수 계산
        criteria_count = sum(bool(re.search(pattern, value)) for pattern in [r'[A-Za-z]', r'[0-9]', r'[@$!%*?&]'])
        
        if criteria_count < 2:
            raise serializers.ValidationError('비밀번호는 영문 대소문자, 숫자, 특수문자 중 2가지 이상 포함해야 합니다.')

        return value

    def validate_password2(self, value):
        """
        비밀번호 확인 유효성 검사: password1과 일치하는지 확인.
        """
        if self.initial_data.get('password1') != value:
            raise serializers.ValidationError('비밀번호가 일치하지 않습니다.')
        return value

    def get_cleaned_data(self):
        """
        기본 cleaned_data에 추가 필드 정보를 포함하여 반환.
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
    


# 회원 정보 수정을 위한 시리얼라이즈
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
        fields = ('pk', 'username', 'email', 'profile_img', 'income', 'career', 'region',)
        read_only_fields = ('email',)

    def update(self, instance, validated_data):
        """
        사용자 정보 업데이트 시 프로필 이미지 처리
        """
        # 프로필 이미지 업데이트 시 기존 이미지 삭제
        if 'profile_img' in validated_data and instance.profile_img:
            instance.profile_img.delete()

        return super().update(instance, validated_data)
    

# 사용자 프로필 정보를 위한 시리얼라이저
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'birthyear', 'profile_img', 'income', 'career', 'region')

    def update(self, instance, validated_data):
        """
        사용자 프로필 정보를 업데이트하는 메서드.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.birthyear = validated_data.get('birthyear', instance.birthyear)
        instance.profile_img = validated_data.get('profile_img', instance.profile_img)
        instance.income = validated_data.get('income', instance.income)
        instance.career = validated_data.get('career', instance.career)
        instance.region = validated_data.get('region', instance.region)
        
        instance.save()
        return instance