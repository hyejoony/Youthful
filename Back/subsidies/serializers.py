from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Subsidy, SubsidyComment

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    user_display_name  = serializers.SerializerMethodField()

    class Meta:
        model = User  # 사용자 모델을 지정
        fields = ('id', 'user_display_name')  # id 필드 추가

    def get_user_display_name (self, obj):
        """닉네임이 있으면 닉네임을 반환하고, 없으면 이메일의 '@' 전까지의 부분을 반환합니다."""
        if obj.nickname:
            return obj.nickname
        return obj.email.split('@')[0] if obj.email else None
    

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

    user_display_name = serializers.SerializerMethodField()

    class Meta:
        model = SubsidyComment
        fields = '__all__'
        read_only_fields = ('user', 'subsidy',)

    def get_user_display_name(self, obj):
        """닉네임이 있으면 닉네임을 반환하고, 없으면 이메일의 '@' 전까지의 부분을 반환합니다."""
        return obj.user.nickname if obj.user.nickname else obj.user.email.split('@')[0]

# 보조금 상세 페이지
class SubsidyDetailSerializers(serializers.ModelSerializer):
    comments = SubsidyCommentListSerializers(many=True, read_only=True)

    class Meta:
        model = Subsidy
        fields = '__all__'