from .models import DepositProduct, DepositOption
from .serializers import DepositProductSerializer, DepositOptionSerializer, DepositProductListSerializers, DepositProductDetailSerializers, UserSerializer

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
def save_deposit(request):
    auth = 'fc98fb30707815d9bfdff7c024175991'
    URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : auth,
        'topFinGrpNo' : '020000',
        'pageNo' : '1'
    }
    response = requests.get(URL, params=params).json()

    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')
        dcls_month = li.get('dcls_month')
        mtrt_int = li.get('mtrt_int')
        max_limit = li.get('max_limit')

        max_limit = max_limit if max_limit else -1


        if DepositProduct.objects.filter(fin_prdt_cd=fin_prdt_cd, kor_co_nm=kor_co_nm,
                                          fin_prdt_nm=fin_prdt_nm, etc_note=etc_note,
                                          join_deny=join_deny, join_member=join_member,
                                          join_way=join_way, spcl_cnd=spcl_cnd, dcls_month=dcls_month,
                                          mtrt_int=mtrt_int, max_limit=max_limit).exists():
            continue


        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'etc_note' : etc_note,
            'join_deny' : join_deny,
            'join_member' : join_member,
            'join_way' : join_way,
            'spcl_cnd' : spcl_cnd,
            'dcls_month' : dcls_month,
            'mtrt_int' : mtrt_int,
            'max_limit' : max_limit,
        }

        serializer = DepositProductSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        intr_rate = li.get('intr_rate')
        intr_rate2 = li.get('intr_rate2')
        save_trm = li.get('save_trm')
        

        intr_rate = intr_rate if intr_rate else -1
        intr_rate2 = intr_rate2 if intr_rate2 else -1


        if DepositOption.objects.filter(fin_prdt_cd=fin_prdt_cd,
                                        intr_rate_type_nm=intr_rate_type_nm,
                                        intr_rate=intr_rate,
                                        intr_rate2=intr_rate2,
                                        save_trm=save_trm).exists():
            continue

        save_data2 = {
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm' : intr_rate_type_nm,
            'intr_rate' : intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm' : save_trm
        }
        
        deposit_product = DepositProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
        serializer2 = DepositOptionSerializer(data=save_data2)
        if serializer2.is_valid(raise_exception=True):
            serializer2.save(deposit_product=deposit_product)

    return JsonResponse({'message' : '저장 성공!'})


# 예금 상품 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_product_list(request):

    # 모든 예금 상품을 가져옵니다.
    deposit_products = get_list_or_404(DepositProduct)

    # 페이지네이션 설정 (선택사항)
    page = request.GET.get('page', 1)
    page_size = 100  # 페이지당 아이템 수
    paginator = Paginator(deposit_products, page_size)
    current_page = paginator.page(page)

    # 시리얼라이저를 사용하여 데이터 직렬화
    serializer = DepositProductListSerializers(current_page, many=True)

    # 페이지네이션 정보 추가
    response_data = {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': int(page),
        'results': serializer.data
    }

    return Response(response_data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_product_detail(request, product_id):
    """
    예금 상품 상세 정보를 조회하는 view 함수
    """
    # 주어진 ID로 예금 상품을 조회합니다. 존재하지 않으면 404 에러를 반환합니다.
    deposit_product = get_object_or_404(DepositProduct, id=product_id)

    # 현재 사용자가 이 상품을 좋아요 했는지 확인합니다.
    is_liked = request.user in deposit_product.like_users.all()

    # 시리얼라이저를 사용하여 데이터 직렬화
    serializer = DepositProductDetailSerializers(deposit_product)

    # 좋아요 정보를 추가합니다.
    response_data = serializer.data
    response_data['is_liked'] = is_liked
    response_data['likes_count'] = deposit_product.like_users.count()

    return Response(response_data, status=status.HTTP_200_OK)


# 좋아요 기능
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_deposit_like(request, product_id):

    deposit_product = get_object_or_404(DepositProduct, id=product_id)
    user = request.user

    if user in deposit_product.like_users.all():
        # 이미 좋아요를 눌렀다면 좋아요 취소
        deposit_product.like_users.remove(user)
        liked = False
    else:
        # 좋아요를 누르지 않았다면 좋아요 추가
        deposit_product.like_users.add(user)
        liked = True

    # 좋아요 처리 후 상품 정보 직렬화
    serializer = DepositProductDetailSerializers(deposit_product)
    # 사용자 정보 직렬화
    like_users_data = UserSerializer(deposit_product.like_users.all(), many=True).data
    
    response_data = serializer.data
    response_data['is_liked'] = liked
    response_data['likes_count'] = deposit_product.like_users.count()
    response_data['like_users'] = like_users_data  # 좋아요한 사용자 정보 추가

    return Response(response_data, status=status.HTTP_200_OK)