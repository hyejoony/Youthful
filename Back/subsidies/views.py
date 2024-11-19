from .models import Subsidy, SubsidyComment
from .serializers import SavingSubsidySerializers, SubsidyListSerializers, SubsidyDetailSerializers, SubsidyCommentListSerializers

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator

from django.conf import settings
from django.http import JsonResponse

# Create your views here.

# DB에 데이터 저장하는 함수
@api_view(['GET'])
def save_subsidy(request):
    serviceKey = '1hNBoDz5YPjnAri1pJlQLBLXpxSc37+ggLtcBm39z4/qPFKNshCARngje1vOQjiekM8GoL71RVoWisZT2JQPLQ=='
    URL = 'https://api.odcloud.kr/api/gov24/v3/serviceDetail'
    params = {
        'serviceKey' : serviceKey,
        'page' : '1',
        'perPage' : '1000'
    }
    response = requests.get(URL, params=params).json()


    for li in response.get('data'):
        name = li.get('서비스명')
        name_category = '기타'
        target = li.get('지원대상')
        content = li.get('지원내용')
        contact = li.get('문의처')

        if Subsidy.objects.filter(name=name, name_category=name_category,
                                    target=target, content=content, contact=contact).exists():
            continue

        save_data = {
            'name' : name,
            'name_category' : name_category,
            'target' : target,
            'content' : content,
            'contact' : contact
        }

        serializer = SavingSubsidySerializers(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({'message' : '저장 성공!'})



# 보조금 상품 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subsidy_list(request):

    # 모든 보조금 상품을 가져옵니다.
    subsidies = get_list_or_404(Subsidy)

    # 페이지네이션 설정 (선택사항)
    page = request.GET.get('page', 1)
    page_size = 10  # 페이지당 아이템 수
    paginator = Paginator(subsidies, page_size)
    current_page = paginator.page(page)

    # 시리얼라이저를 사용하여 데이터 직렬화
    serializer = SubsidyListSerializers(current_page, many=True)

    # 페이지네이션 정보 추가
    response_data = {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': int(page),
        'results': serializer.data
    }

    return Response(response_data, status=status.HTTP_200_OK)


# 보조금 상세 페이지
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subsidy_detail(request, subsidy_id):

    # 주어진 ID로 보조금을 조회합니다. 존재하지 않으면 404 에러를 반환합니다.
    subsidy = get_object_or_404(Subsidy, id=subsidy_id)

    # 현재 사용자가 이 상품을 좋아요 했는지 확인합니다.
    is_liked = request.user in subsidy.like_users.all()

    # 시리얼라이저를 사용하여 데이터 직렬화
    serializer = SubsidyDetailSerializers(subsidy)

    # 좋아요 정보를 추가합니다.
    response_data = serializer.data
    response_data['is_liked'] = is_liked
    response_data['likes_count'] = subsidy.like_users.count()

    return Response(response_data, status=status.HTTP_200_OK)


# POST - 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, subsidy_id):
    subsidy = get_object_or_404(Subsidy, pk=subsidy_id)
    
    if request.method == 'POST':
        serializer = SubsidyCommentListSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, subsidy=subsidy)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# DELETE - 리뷰 삭제
# PUT - 리뷰 수정
@api_view(['DELETE', 'PUT'])
def comment_detail(request, subsidy_id, comment_id):
    comment = get_object_or_404(SubsidyComment, pk=comment_id)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = SubsidyCommentListSerializers(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 좋아요 기능
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_subsidy_like(request, subsidy_id):

    subsidy = get_object_or_404(Subsidy, id=subsidy_id)
    user = request.user

    if user in subsidy.like_users.all():
        # 이미 좋아요를 눌렀다면 좋아요 취소
        subsidy.like_users.remove(user)
        liked = False
    else:
        # 좋아요를 누르지 않았다면 좋아요 추가
        subsidy.like_users.add(user)
        liked = True

    # 좋아요 처리 후 상품 정보 직렬화
    serializer = SubsidyDetailSerializers(subsidy)
    
    response_data = serializer.data
    response_data['is_liked'] = liked
    response_data['likes_count'] = subsidy.like_users.count()

    return Response(response_data, status=status.HTTP_200_OK)