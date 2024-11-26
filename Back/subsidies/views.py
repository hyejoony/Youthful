from .models import Subsidy, SubsidyComment
from .serializers import SavingSubsidySerializers, SubsidyListSerializers, SubsidyDetailSerializers, SubsidyCommentListSerializers, UserSerializer

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
        'perPage' : '2000'
    }
    response = requests.get(URL, params=params).json()


    for li in response.get('data'):
        name = li.get('서비스명')
        # name_category = '기타'
        target = li.get('지원대상')
        content = li.get('지원내용')
        contact = li.get('문의처')
        # 카테고리 결정
        if any(keyword in name for keyword in ["학비", "교육", "유아", "학생", "보육", "교사"]):
            name_category = "교육"
        elif any(keyword in name for keyword in ["장려금", "지원금", "보조금", "융자", "대출", "세금 감면"]):
            name_category = "재정"
        elif any(keyword in name for keyword in ["주택", "월세", "보증금", "주거", "생활비"]):
            name_category = "주택 및 생활"
        elif any(keyword in name for keyword in ["친환경", "에너지 절감", "환경 보호", "신재생 에너지"]):
            name_category = "환경 및 에너지"
        elif any(keyword in name for keyword in ["어업", "수산물", "양식", "해양"]):
            name_category = "어업 및 수산업"
        elif any(keyword in name for keyword in ["법률", "복지", "상담", "피해자"]):
            name_category = "법률 및 복지"
        elif any(keyword in name for keyword in ["취약계층", "노인", '여성']):
            name_category = '취약계층'
        elif any(keyword in name for keyword in ["농업","농촌","농민"]):
            name_category = '농업'
        elif any(keyword in name for keyword in ["1인", "청년" "1인 가구"]):
            name_category = '청년 1인'
        else:
            name_category = '기타'
        

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
    page_size = 100  # 페이지당 아이템 수
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


from django.forms.models import model_to_dict
# 보조금 추천 상품 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subsidy_recommend_list(request):
    subsidies = get_list_or_404(Subsidy)
    serializers = SubsidyListSerializers(subsidies, many=True)
    reco_subsidies = []

    current_user = request.user
    # 현재 유저의 모든 필드를 딕셔너리로 변환
    current_user_data = model_to_dict(current_user)

    for serializer in serializers.data:
        # print(serializer)
        cnt = 0
        if len(serializer['liked_users_info']) > 0:
            for like_user in serializer['liked_users_info']:
                # print('아아아', like_user['birthyear'])
                # print('아아아2', current_user_data['birthyear'])
                if current_user_data['birthyear']-5 <= like_user['birthyear'] <= current_user_data['birthyear']+5:
                    cnt += 2
                if like_user['income'] == current_user_data['income']:
                    cnt += 2
                if like_user['career'] == current_user_data['career']:
                    cnt += 1
                if like_user['region'] == current_user_data['region']:
                    cnt += 1
            reco_subsidies.append((cnt, serializer))
        else:
            reco_subsidies.append((0, serializer))
    # 정렬 시, 점수를 기준으로 정렬
    reco_subsidies.sort(key=lambda x: x[0], reverse=True)

    return Response([subsidy for _, subsidy in reco_subsidies], status=status.HTTP_200_OK)


# 보조금 상세 페이지
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def subsidy_detail(request, subsidy_id):
    # 주어진 ID로 보조금을 조회합니다. 존재하지 않으면 404 에러를 반환합니다.
    subsidy = get_object_or_404(Subsidy, id=subsidy_id)
    if request.method == 'GET':
        # 현재 사용자가 이 상품을 좋아요 했는지 확인합니다.
        is_liked = request.user in subsidy.like_users.all()

        # 시리얼라이저를 사용하여 데이터 직렬화
        serializer = SubsidyDetailSerializers(subsidy)
        # 사용자 정보 직렬화
        like_users_data = UserSerializer(subsidy.like_users.all(), many=True).data

        # 좋아요 정보를 추가합니다.
        response_data = serializer.data
        response_data['is_liked'] = is_liked
        response_data['likes_count'] = subsidy.like_users.count()
        response_data['like_users'] = like_users_data  # 좋아요한 사용자 정보 추가

        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
            # 좋아요/취소 액션 처리
            action = request.data.get('action')
            
            if action == 'like':
                # 좋아요 추가
                if request.user not in subsidy.like_users.all():
                    subsidy.like_users.add(request.user)
            elif action == 'unlike':
                # 좋아요 취소
                if request.user in subsidy.like_users.all():
                    subsidy.like_users.remove(request.user)
            else:
                return Response({'error': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # 업데이트된 좋아요 정보 반환
            return Response({
                'is_liked': request.user in subsidy.like_users.all(),
                'likes_count': subsidy.like_users.count()
            }, status=status.HTTP_200_OK)


# POST - 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, subsidy_id):
    subsidy = get_object_or_404(Subsidy, pk=subsidy_id)
    
    if request.method == 'POST':
        serializer = SubsidyCommentListSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, subsidy=subsidy)
            response_data = serializer.data
            response_data['user_display_name'] = serializer.get_user_display_name(serializer.instance)
            return Response(response_data, status=status.HTTP_201_CREATED)
        

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
    # 사용자 정보 직렬화
    like_users_data = UserSerializer(subsidy.like_users.all(), many=True).data
    
    response_data = serializer.data
    response_data['is_liked'] = liked
    response_data['likes_count'] = subsidy.like_users.count()
    response_data['like_users'] = like_users_data  # 좋아요한 사용자 정보 추가

    return Response(response_data, status=status.HTTP_200_OK)