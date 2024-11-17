from rest_framework import serializers
from .models import Community, CommunityComment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

# 커뮤니티 전체 목록 페이지
class CommunityListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Community
        fields = ('id', 'title', 'keyword', 'username')






class CommunityListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Community
        fields = ('id', 'title', 'keyword', 'content', 'created_at', 'username')

class CommunityDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    communitycomment_set = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = ('id', 'title', 'keyword', 'content', 'created_at', 'updated_at', 'username', 'communitycomment_set')

    def get_communitycomment_set(self, obj):
        # 여기에 댓글을 가져오는 로직을 구현합니다.
        # 예를 들어:
        comments = obj.communitycomment_set.all()
        return CommentSerializer(comments, many=True).data

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = CommunityComment  # CommunityComment 모델이 정의되어 있다고 가정
        fields = ('id', 'content', 'created_at', 'username')