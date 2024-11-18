from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomRegisterSerializer
from dj_rest_auth.registration.views import RegisterView

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
