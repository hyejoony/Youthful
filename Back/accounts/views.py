from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from .serializers import CustomRegisterSerializer, CustomUserDetailsSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser
from django.db import transaction
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


User = get_user_model()

# Create your views here.
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def register(request):
    """
    회원가입 API 엔드포인트

    처리 과정:
    1. 요청 데이터 유효성 검사
    2. 사용자 생성 및 추가 정보 저장
    3. 프로필 이미지 처리
    4. 응답 반환

    요청 데이터:
    - email: 이메일 (필수)
    - password1: 비밀번호 (필수)
    - password2: 비밀번호 확인 (필수)
    - nickname: 닉네임 (선택)
    - profile_image: 프로필 이미지 파일 (선택)
    """
    try:
        with transaction.atomic():
            # 데이터 유효성 검사
            serializer = CustomRegisterSerializer(data=request.data)
            
            if not serializer.is_valid():
                return Response(
                    {'detail': serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # 사용자 생성
            user = serializer.save(request)
            # 응답 데이터 생성
            user_data = CustomUserDetailsSerializer(user).data

            # 절대 URL 생성 (이미지)
            if user_data.get('profile_image'):
                user_data['profile_image'] = request.build_absolute_uri(
                    user.profile_image.url
                )
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'detail': '회원가입이 완료되었습니다.',
                'user': user_data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)

    except ValidationError as e:
        return Response({
            'detail': str(e),
            'code': 'validation_error'
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'detail': '회원가입 처리 중 오류가 발생했습니다.',
            'code': 'server_error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# GET - 현재 사용자의 프로필 정보
# PUT - 현재 사용자의 회원정보 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request, user_id):

    cur_user = request.user
    user = get_object_or_404(User, id=user_id)

    if request.method == 'GET':
        is_self = user == cur_user
        serializer = CustomUserDetailsSerializer(user)
        data = serializer.data
        data['is_self'] = is_self

        return Response(data)

    elif request.method == 'PUT':
        serializer = CustomUserDetailsSerializer(cur_user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
