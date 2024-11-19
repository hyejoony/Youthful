from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import CommunityListSerializer, CommunityCommentListSerializer, CommunityDetailSerializer
from .models import Community, CommunityComment


# GET - 게시글 조회 (전체 목록 페이지 버전)
# POST - 게시글 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def community_list(request):
    if request.method == 'GET':
        communities = get_list_or_404(Community)
        serializer = CommunityListSerializer(communities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommunityDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# GET - 게시글 조회 (상세 페이지 버전)
# DELETE - 게시글 삭제
# PUT - 게시글 수정
@api_view(['GET', 'DELETE', 'PUT'])
def community_detail(request, community_id):
    community = get_object_or_404(Community, pk=community_id)

    if request.method == 'GET':
        serializer = CommunityDetailSerializer(community)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommunityDetailSerializer(community, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# POST - 댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    
    if request.method == 'POST':
        serializer = CommunityCommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, community=community)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# DELETE - 댓글 삭제
# PUT - 댓글 수정
@api_view(['DELETE', 'PUT'])
def comment_detail(request, community_id, comment_id):
    comment = get_object_or_404(CommunityComment, pk=comment_id)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommunityCommentListSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)