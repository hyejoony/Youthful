from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Community, CommunityComment

User = get_user_model()

# 커뮤니티 전체 목록 시리얼라이즈
class CommunityListSerializer(serializers.ModelSerializer):

    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Community
        fields = ('id' ,'user', 'title', 'keyword','comments_count', 'updated_at')


# 댓글 생성, 수정 시리얼라이즈
class CommunityCommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityComment
        fields = '__all__'
        read_only_fields = ('user', 'community',)


# 커뮤니티 상세, 생성, 수정 시리얼라이즈
class CommunityDetailSerializer(serializers.ModelSerializer):

    # 댓글 조회
    comments = CommunityCommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = '__all__'
        read_only_fields = ('user',)