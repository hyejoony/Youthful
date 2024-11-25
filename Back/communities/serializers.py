from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Community, CommunityComment

User = get_user_model()

# 유저의 이름을 나타내기 위한 시리얼라이즈
class UserDisplayNameSerializer(serializers.ModelSerializer):
    user_display_name = serializers.SerializerMethodField()

    class Meta:
        fields = ('user_display_name',)  # user_display_name 필드만 포함

    def get_user_display_name(self, obj):
        """닉네임이 있으면 닉네임을 반환하고, 없으면 이메일의 '@' 전까지의 부분을 반환합니다."""
        if obj.user.nickname == 'null':  # 해당 값이 null값이므로 조건을 이렇게 달아줘야 한다
            return obj.user.email.split('@')[0]
        return obj.user.nickname


# 커뮤니티 전체 목록 시리얼라이즈
class CommunityListSerializer(UserDisplayNameSerializer):
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta(UserDisplayNameSerializer.Meta):
        model = Community
        fields = UserDisplayNameSerializer.Meta.fields + ('id', 'user_display_name', 'title', 'keyword', 'comments_count', 'updated_at')


# 댓글 생성, 수정 시리얼라이즈
class CommunityCommentListSerializer(UserDisplayNameSerializer):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = CommunityComment
        fields = '__all__'
        read_only_fields = ('user', 'community',)
        
    def get_profile_image(self, obj):
        if obj.user.profile_image:
            return obj.user.profile_image.url
        return None  # 또는 기본 이미지 URL을 반환할 수 있습니다.


# 커뮤니티 상세, 생성, 수정 시리얼라이즈
class CommunityDetailSerializer(UserDisplayNameSerializer):
    comments = CommunityCommentListSerializer(many=True, read_only=True)
    profile_image = serializers.SerializerMethodField()

    class Meta(UserDisplayNameSerializer.Meta):
        model = Community
        fields = '__all__'
        read_only_fields = ('user_display_name', 'user', 'profile_image')

    def get_profile_image(self, obj):
        if obj.user.profile_image:
            return obj.user.profile_image.url
        return None  # 또는 기본 이미지 URL을 반환할 수 있습니다.