from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Subsidy, SubsidyComment

User = get_user_model()


# 보조금 상품 저장 시리얼라이즈
class SavingSubsidySerializers(serializers.ModelSerializer):

    class Meta:
        model = Subsidy
        fields = '__all__'

# 보조금 목록 페이지
class SubsidyListSerializers(serializers.ModelSerializer):

    likes_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Subsidy
        fields = ('id' ,'name', 'name_category', 'target', 'contact', 'likes_count')

# 특정 보조금 리뷰 조회, 생성, 수정
class SubsidyCommentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubsidyComment
        fields = '__all__'
        read_only_fields = ('user', 'subsidy',)

# 보조금 상세 페이지
class SubsidyDetailSerializers(serializers.ModelSerializer):

    comments = SubsidyCommentListSerializers(many=True, read_only=True)

    class Meta:
        model = Subsidy
        fields = '__all__'