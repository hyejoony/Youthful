from django.urls import path, include
from .views import CustomRegisterView

urlpatterns = [
    # dj-rest-auth 라이브러리의 기본 인증 관련 URL 패턴들을 포함
    # 이는 로그인, 로그아웃, 비밀번호 재설정 등의 엔드포인트를 제공합니다
    path('', include('dj_rest_auth.urls')),

    # 커스텀 회원가입 뷰를 'signup/' URL에 연결
    # CustomRegisterView는 우리가 정의한 커스텀 회원가입 로직을 처리합니다
    path('signup/', CustomRegisterView.as_view()),
] 
