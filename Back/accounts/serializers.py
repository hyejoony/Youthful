from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from PIL import Image
import base64
import uuid
import os
from django.core.validators import MinValueValidator, MaxValueValidator
from allauth.account.adapter import get_adapter
from dj_rest_auth.serializers import UserDetailsSerializer
import re

from deposits.models import DepositProduct
from savings.models import SavingProduct
from subsidies.models import Subsidy


User = get_user_model()

ALLOWED_IMAGE_TYPES = ['JPEG', 'JPG', 'PNG']
MAX_UPLOAD_SIZE = 2 * 1024 * 1024  # 2MB

# 소득 수준 선택 옵션
INCOME_CHOICES = [
    ('0~50%', '약 100만원'),
    ('51~75%', '약 150만원'),
    ('76~100%', '약 200만원'),
    ('101~200%', '약 450만원'),
    ('200%~', '약 450만원 초과'),
]

# 직업 선택 옵션
CAREER_CHOICES = [
    ('학생', 'student'),
    ('회사원', 'office_worker'),
    ('사업자', 'business_owner'),
    ('아르바이트/비정규직', 'part_time'),
    ('무직/구직중', 'unemployed'),
    ('군인', 'soldier'),
    ('스타트업 창업자', 'startup_founder'),
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

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100,
        help_text='선택적 닉네임 필드'
    )
    profile_image = serializers.ImageField(
        required=False,
        allow_null=True,
        help_text='프로필 이미지 (JPEG/PNG, 최대 2MB)'
    )
    # 생년 필드: 1900년 이상 9999년 이하의 정수만 허용
    birthyear = serializers.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(9999)],
    )
    
    # 소득, 경력, 지역 필드: 선택 가능한 값들 정의
    income = serializers.ChoiceField(choices=INCOME_CHOICES)
    career = serializers.ChoiceField(choices=CAREER_CHOICES)
    region = serializers.ChoiceField(choices=REGION_CHOICES)
    
    # 약관 동의 필드: 기본값은 False
    condition1 = serializers.BooleanField(default=False)
    condition2 = serializers.BooleanField(default=False)

    # username 필드 제거
    username = None

    def validate_profile_image(self, image_data):
        """이미지 유효성 검사 및 처리"""
        if not image_data:
            return None

        try:
            # Base64 이미지 처리
            if isinstance(image_data, str) and 'data:image' in image_data:
                # Base64 디코딩 및 이미지 추출
                format, imgstr = image_data.split(';base64,')
                ext = format.split('/')[-1].upper()

                if ext not in ALLOWED_IMAGE_TYPES:
                    raise serializers.ValidationError(
                        f'지원되지 않는 이미지 형식입니다. 허용된 형식: {", ".join(ALLOWED_IMAGE_TYPES)}'
                    )

                # 이미지 생성 및 검증
                image_data = ContentFile(base64.b64decode(imgstr))
                img = Image.open(image_data)

            # 일반 파일 업로드 처리
            else:
                img = Image.open(image_data)
                if img.format.upper() not in ALLOWED_IMAGE_TYPES:
                    raise serializers.ValidationError(
                        f'지원되지 않는 이미지 형식입니다. 허용된 형식: {", ".join(ALLOWED_IMAGE_TYPES)}'
                    )

            # 이미지 크기 검증
            if image_data.size > MAX_UPLOAD_SIZE:
                raise serializers.ValidationError(
                    f'이미지 크기는 {MAX_UPLOAD_SIZE / 1024 / 1024}MB를 초과할 수 없습니다.'
                )

            # 이미지 무결성 검증
            img.verify()
            return image_data

        except Exception as e:
            raise serializers.ValidationError(f'이미지 처리 중 오류가 발생했습니다: {str(e)}')

    def validate(self, data):
        """전체 데이터 유효성 검사"""
        data = super().validate(data)
        password = data.get('password1')

        # 비밀번호 길이 검사
        if len(password) < 8 or len(password) > 20:
            raise serializers.ValidationError({
                'password1': '비밀번호는 8자에서 20자 사이여야 합니다.'
            })

        # 비밀번호 복잡성 검사
        complexity_checks = [
            (r'[A-Z]', '대문자'),
            (r'[a-z]', '소문자'),
            (r'\d', '숫자'),
            (r'[!@#$%^&*(),.?":{}|<>]', '특수문자')
        ]

        passed_checks = sum(bool(re.search(pattern, password)) for pattern, _ in complexity_checks)

        if passed_checks < 2:
            error_message = '비밀번호는 다음 중 최소 2가지를 포함해야 합니다: 영문 대문자, 영문 소문자, 숫자, 특수문자'
            raise serializers.ValidationError({
                'password1': error_message
            })
        
        # condition1 검사
        if not data.get('condition1'):
            raise serializers.ValidationError({
                'condition1': '필수 동의 항목입니다.'
            })

        # condition2 검사
        if not data.get('condition2'):
            raise serializers.ValidationError({
                'condition2': '필수 동의 항목입니다.'
            })

        return data



    def get_cleaned_data(self):
        """검증된 데이터 반환"""
        data = super().get_cleaned_data()
        data.update({
            'nickname': self.validated_data.get('nickname', ''),
            'profile_image': self.validated_data.get('profile_image', None),
            'birthyear': self.validated_data.get('birthyear', ''),
            'income': self.validated_data.get('income', ''),
            'career': self.validated_data.get('career', ''),
            'region': self.validated_data.get('region', ''),
            'condition1': self.validated_data.get('condition1', False),
            'condition2': self.validated_data.get('condition2', False),
        })
        return data

    def save(self, request):
        """사용자 저장 및 추가 정보 처리"""
        try:
            adapter = get_adapter()
            user = adapter.new_user(request)
            self.cleaned_data = self.get_cleaned_data()

            # 기본 사용자 정보 저장
            user.email = self.cleaned_data.get('email')
            user.set_password(self.cleaned_data.get('password1'))

            # 추가 필드 저장
            user.nickname = self.cleaned_data.get('nickname', '')
            user.birthyear = self.cleaned_data.get('birthyear', '')
            user.income = self.cleaned_data.get('income', '')
            user.career = self.cleaned_data.get('career', '')
            user.region = self.cleaned_data.get('region', '')
            user.condition1 = self.cleaned_data.get('condition1', False)
            user.condition2 = self.cleaned_data.get('condition2', False)
            print('nick')
            # 프로필 이미지 처리
            image_data = self.cleaned_data.get('profile_image', None)
            print(image_data)
            if image_data:
                if isinstance(image_data, str) and 'data:image' in image_data:
                    # Base64 이미지 처리

                    format, imgstr = image_data.split(';base64,')
                    ext = format.split('/')[-1]
                    file_name = f"{uuid.uuid4()}.{ext}"
                    image_content = ContentFile(base64.b64decode(imgstr), name=file_name)
                    user.profile_image.save(file_name, image_content, save=False)
                else:
                    # 일반 파일 업로드 처리
                    ext = os.path.splitext(image_data.name)[1]
                    file_name = f"{uuid.uuid4()}{ext}"
                    user.profile_image.save(file_name, image_data, save=False)
      
      
            user.save()
            return user

        except Exception as e:
            raise serializers.ValidationError(f'사용자 저장 중 오류가 발생했습니다: {str(e)}')
    

# 찜한 예금 가져오기 위한 시리얼라이즈
class LikeDepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = ('id', 'fin_prdt_nm')  # 금융 상품 ID와 이름만 포함

# 찜한 적금 가져오기 위한 시리얼라이즈
class LikeSavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = ('id', 'fin_prdt_nm')  # 금융 상품 ID와 이름만 포함

# 찜한 지원금 가져오기 위한 시리얼라이즈
class LikeSubsidySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsidy
        fields = ('id', 'name')  # 금융 상품 ID와 키워드만 포함



# 회원 정보 수정을 위한 시리얼라이즈
# 회원 프로필 정보를 위한 시리얼라이저
class CustomUserDetailsSerializer(UserDetailsSerializer):
    profile_image = serializers.ImageField(
        required=False,
        allow_null=True,
        help_text='프로필 이미지 (JPEG/PNG, 최대 2MB)'
    )
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100,
        help_text='사용자 닉네임'
    )
    # 생년 필드: 1900년 이상 9999년 이하의 정수만 허용
    birthyear = serializers.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(9999)],
    )
    
    # 소득, 경력, 지역 필드: 선택 가능한 값들 정의
    income = serializers.ChoiceField(choices=INCOME_CHOICES)
    career = serializers.ChoiceField(choices=CAREER_CHOICES)
    region = serializers.ChoiceField(choices=REGION_CHOICES)
    like_deposits = LikeDepositProductSerializer(many=True, read_only=True)
    like_savings = LikeSavingProductSerializer(many=True, read_only=True)
    like_subsidies = LikeSubsidySerializer(many=True, read_only=True)

    # username 필드 제거
    username = None

    class Meta:
        model = User
        fields = ('pk', 'email', 'nickname', 'profile_image', 'birthyear', 
                  'income', 'career', 'region', 'like_deposits', 'like_savings', 'like_subsidies')
        read_only_fields = ('email',)
        
    def validate_profile_image(self, image_data):
        """프로필 이미지 유효성 검사"""
        if not image_data:
            return None

        return CustomRegisterSerializer.validate_profile_image(self, image_data)
    
    def update(self, instance, validated_data):
        """사용자 정보 업데이트"""
        try:
            if 'profile_image' in validated_data:
                # 기존 이미지 삭제
                if instance.profile_image:
                    # 실제 파일 삭제
                    old_image_path = instance.profile_image.path
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
                    # 필드 초기화
                    instance.profile_image = None

                # 새 이미지 저장
                new_image = validated_data.pop('profile_image')
                if new_image:
                    instance.profile_image = new_image

            # 다른 필드 업데이트
            instance.nickname = validated_data.get('nickname', instance.nickname)
            instance.profile_image = validated_data.get('profile_image', instance.profile_image)
            instance.birthyear = validated_data.get('birthyear', instance.birthyear)
            instance.income = validated_data.get('income', instance.income)
            instance.career = validated_data.get('career', instance.career)
            instance.region = validated_data.get('region', instance.region)

            instance.save()
            return instance

        except Exception as e:
            raise serializers.ValidationError(f'프로필 업데이트 중 오류가 발생했습니다: {str(e)}')
    
# 유저의 id값 가져오는 시리얼라이즈
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', )# 필요한 필드 추가