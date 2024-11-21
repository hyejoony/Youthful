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
        if obj.user.nickname:
            return obj.user.nickname
        return obj.user.email.split('@')[0] if obj.user.email else None


# 커뮤니티 전체 목록 시리얼라이즈
class CommunityListSerializer(UserDisplayNameSerializer):
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta(UserDisplayNameSerializer.Meta):
        model = Community
        fields = UserDisplayNameSerializer.Meta.fields + ('id', 'user_display_name', 'title', 'keyword', 'comments_count', 'updated_at')


# 댓글 생성, 수정 시리얼라이즈
class CommunityCommentListSerializer(UserDisplayNameSerializer):
    class Meta:
        model = CommunityComment
        fields = '__all__'
        read_only_fields = ('user', 'community',)


# 커뮤니티 상세, 생성, 수정 시리얼라이즈
class CommunityDetailSerializer(UserDisplayNameSerializer):
    comments = CommunityCommentListSerializer(many=True, read_only=True)

    class Meta(UserDisplayNameSerializer.Meta):
        model = Community
        fields = '__all__'
        read_only_fields = ('user_display_name','user')