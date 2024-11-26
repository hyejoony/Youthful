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

# 보조금 상품 목록 페이지
class SubsidyListSerializers(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='like_users.count', read_only=True)
    liked_users_info = serializers.SerializerMethodField()
    current_user_info = serializers.SerializerMethodField()

    class Meta:
        model = Subsidy
        fields = ('id', 'name', 'name_category', 'target', 'contact', 'likes_count', 'liked_users_info', 'current_user_info')

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

    def get_current_user_info(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            return {
                'birthyear': user.birthyear,
                'career': user.career,
                'region': user.region,
                'income': user.income,
                'user_display_name': self.get_user_display_name(user)
            }
        return None

    def get_user_display_name(self, user):
        if user.nickname:
            return user.nickname
        return user.email.split('@')[0] if user.email else None
    
    

# 특정 보조금 리뷰 조회, 생성, 수정
class SubsidyCommentListSerializers(serializers.ModelSerializer):

    user_display_name = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = SubsidyComment
        fields = '__all__'
        read_only_fields = ('user', 'subsidy', 'profile_image')

    def get_user_display_name(self, obj):
        """닉네임이 있으면 닉네임을 반환하고, 없으면 이메일의 '@' 전까지의 부분을 반환합니다."""
        if obj.user.nickname == 'null':  # 해당 값이 null값이므로 조건을 이렇게 달아줘야 한다
            return obj.user.email.split('@')[0]
        return obj.user.nickname
    
    def get_profile_image(self, obj):
        if obj.user.profile_image:
            return obj.user.profile_image.url
        return None  # 또는 기본 이미지 URL을 반환할 수 있습니다.

# 보조금 상세 페이지
class SubsidyDetailSerializers(serializers.ModelSerializer):
    comments = SubsidyCommentListSerializers(many=True, read_only=True)

    class Meta:
        model = Subsidy
        fields = '__all__'