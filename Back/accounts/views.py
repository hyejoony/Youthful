from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomRegisterSerializer, CustomUserDetailsSerializer
from dj_rest_auth.registration.views import RegisterView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class CustomRegisterView(RegisterView):
    """
    커스텀 회원가입 뷰

    dj-rest-auth의 RegisterView를 상속받아 커스터마이즈한 회원가입 뷰입니다.
    CustomRegisterSerializer를 사용하여 추가 필드를 포함한 회원가입 프로세스를 처리합니다.
    """
    serializer_class = CustomRegisterSerializer
    # CustomRegisterSerializer를 이 뷰의 시리얼라이저로 지정합니다.
    # 이를 통해 기본 회원가입 필드 외에 추가적인 사용자 정보를 처리할 수 있습니다.


# GET - 현재 사용자의 프로필 정보
# PUT - 현재 사용자의 회원정보 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):

    user = request.user

    if request.method == 'GET':
        serializer = CustomUserDetailsSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomUserDetailsSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)