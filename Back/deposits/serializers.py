from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import DepositProduct, DepositOption

User = get_user_model()

# 예금 상품 저장 시리얼라이즈
class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'


# 예금 상품 옵션 저장 시리얼라이즈
class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ('deposit_product',)


# 예금 상품 목록 페이지
class DepositProductListSerializers(serializers.ModelSerializer):

    # 예금 상품 목록 페이지에 필요한 예금 옵션 정보
    class DepositOptionListSerializers(serializers.ModelSerializer):
        class Meta:
            model = DepositOption
            fields = ('id', 'save_trm', 'intr_rate2')
    
    deposit_options = DepositOptionListSerializers(many=True, read_only=True)
    likes_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = DepositProduct
        fields = ('id', 'kor_co_nm', 'fin_prdt_nm', 'deposit_options', 'likes_count')


# 예금 상품 상세 페이지
class DepositProductDetailSerializers(serializers.ModelSerializer):

    # 예금 상품 상세 페이지에 필요한 예금 옵션 정보
    class DepositOptionDetailSerializers(serializers.ModelSerializer):
        class Meta:
            model = DepositOption
            fields = '__all__'
    
    deposit_detail_options = DepositOptionDetailSerializers(many=True, read_only=True)
    
    class Meta:
            model = DepositProduct
            fields = '__all__'