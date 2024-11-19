from .models import DepositProduct, DepositOption
from .serializers import DepositProductSerializer, DepositOptionSerializer, DepositProductListSerializers, DepositProductDetailSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests

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