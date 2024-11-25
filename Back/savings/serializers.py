from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import SavingProduct, SavingOption

User = get_user_model()


# 유저의 이름을 나타내기 위한 시리얼라이즈
class UserSerializer(serializers.ModelSerializer):
    user_display_name = serializers.SerializerMethodField()

    class Meta:
        model = User  # 사용자 모델을 지정
        fields = ('id', 'user_display_name',)

    def get_user_display_name(self, obj):
        """닉네임이 있으면 닉네임을 반환하고, 없으면 이메일의 '@' 전까지의 부분을 반환합니다."""
        if obj.nickname:
            return obj.nickname
        return obj.email.split('@')[0] if obj.email else None
    

# 적금 상품 저장 시리얼라이즈
class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'


# 적금 상품 옵션 저장 시리얼라이즈
class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('saving_product',)


# 적금 상품 목록 페이지
class SavingProductListSerializers(serializers.ModelSerializer):
    
    # 적금 상품 목록 페이지에 필요한 적금 옵션 정보
    class SavingOptionListSerializers(serializers.ModelSerializer):
        class Meta:
            model = SavingOption
            fields = ('id', 'save_trm', 'intr_rate2')
    
    saving_options = SavingOptionListSerializers(many=True, read_only=True)
    likes_count = serializers.IntegerField(source='like_users.count', read_only=True)
    liked_users_info = serializers.SerializerMethodField()

    class Meta:
        model = SavingProduct
        fields = ('id', 'kor_co_nm', 'fin_prdt_nm', 'saving_options', 'likes_count', 'liked_users_info')

    def get_liked_users_info(self, obj):
        return [
            {
                'birthyear': user.birthyear,
                'income': user.income,
                'career': user.career,
                'region': user.region
            }
            for user in obj.like_users.all()
        ]


# 적금 상품 상세 페이지
class SavingProductDetailSerializers(serializers.ModelSerializer):

    # 적금 상품 상세 페이지에 필요한 적금 옵션 정보
    class SavingOptionDetailSerializers(serializers.ModelSerializer):
        class Meta:
            model = SavingOption
            fields = '__all__'
    
    saving_options = SavingOptionDetailSerializers(many=True, read_only=True)
    class Meta:
            model = SavingProduct
            fields = '__all__'