from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpRequest
import re # 정규표현식 


# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ExchangeSerializers
from .models import Exchange

import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse

# DB에 데이터 저장하는 함수 (크롤링)
@api_view(['GET'])
def save_exchange(request):
    # 네이버 환율 정보 페이지 URL
    URL = 'https://finance.naver.com/marketindex/exchangeList.naver'
    
    # 해당 URL에 GET 요청을 보내고 응답을 받음
    response = requests.get(URL)
    
    # 응답받은 HTML 콘텐츠를 BeautifulSoup를 사용하여 파싱
    soup = BeautifulSoup(response.content, 'html.parser')

    # 모든 <tr> 태그를 찾아서 행(row) 리스트를 생성
    rows = soup.find_all('tr')

    # 각 행(row)을 반복하여 환율 정보를 추출
    for row in rows:
        # 각 행에서 <td> 태그를 찾아 열(column) 리스트를 생성
        columns = row.find_all('td')
        
        # 열의 개수가 7개 이상인 경우에만 데이터 처리 (헤더 행 제외)
        if len(columns) >= 7:

            country_currency = columns[0].text.strip() #나라명, 화폐단위
        # 국가명, 통화 단위, 단위 정보 분리
            match = re.match(r'(.+)\s+([A-Z]{3})\s*(\(.+\))?', country_currency)
            if match:
                country_name = match.group(1).strip()
                cur_unit = match.group(2)
            else:
                country_name = country_currency
                cur_unit = "N/A"
                

            # 링크 추출
            link_pre = columns[0].find('a')['href']
            link = f'https://finance.naver.com{link_pre}'  # 전체 URL 생성

            
            basic_rate = columns[1].text.strip()  # 매매 기준율
            cash_send = columns[2].text.strip()  # 현찰 살때 환율
            cash_receive = columns[3].text.strip()  # 현찰 팔때 환율

            # 추가 크롤링: 상세 페이지에서 이미지 링크 가져오기
            img_src = get_image_src(link)

            # 저장할 데이터를 딕셔너리 형태로 구성
            save_data = {
                'country_name': country_name,
                'cur_unit': cur_unit,
                'link': link,
                'image_src': img_src,  # 이미지 링크 추가
                'basic_rate': basic_rate,
                'cash_send': cash_send,
                'cash_receive': cash_receive
            }

            # 시리얼라이저를 사용하여 데이터를 검증 및 저장
            serializer = ExchangeSerializers(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()  # 데이터베이스에 저장

    # 모든 데이터가 성공적으로 저장되었음을 알리는 JSON 응답 반환
    return JsonResponse({'message': '저장 성공!'})

def get_image_src(url):
    """
    주어진 URL에서 이미지 링크를 크롤링하여 반환하는 함수.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # flash_area 클래스가 있는 div 태그 안의 img 태그 찾기
    flash_area = soup.find('div', class_='flash_area')
    
    if flash_area:
        img_tag = flash_area.find('img')  # img 태그 찾기
        
        if img_tag and 'src' in img_tag.attrs:
            return img_tag['src']  # src 속성 반환
    
    return None  # 이미지가 없으면 None 반환


# GET - 환율 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def exchange_list(request):
    if request.method == 'GET':
        exchanges = get_list_or_404(Exchange)
        serializer = ExchangeSerializers(exchanges, many=True)
        return Response(serializer.data)
    
#매일 특정시간에 데이터 새로고침
@api_view(['DELETE'])
def clear_list(request):
    exchanges = Exchange.objects.all()
    exchanges.delete()
    # HttpRequest 객체 생성하여 전달
    http_request = HttpRequest()
    http_request.method = 'GET'  # save_exchange는 GET 메소드를 기대합니다
    
    # 새로운 데이터 저장
    save_exchange(http_request)
    if request:
        return Response({'message': '데이터 초기화 및 새로고침 완료'}, status=status.HTTP_200_OK)
        
    