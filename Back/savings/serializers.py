from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import SavingProduct, SavingOption

User = get_user_model()

# 적금 상품 목록 페이지
class SavingProductListSerializers(serializers.ModelSerializer):

    # 적금 상품 목록 페이지에 필요한 적금 옵션 정보
    class SavingOptionListSerializers(serializers.ModelSerializer):
        class Meta:
            model = SavingOption
            fields = ('id', 'save_trm', 'intr_rate2')
    
    saving_options = SavingOptionListSerializers(many=True, read_only=True)
    likes_count = serializers.IntegerField(source='like_savings.count', read_only=True)

    class Meta:
        model = SavingProduct
        fields = ('id', 'kor_co_nm', 'fin_prdt_nm', 'saving_options', 'likes_count')


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