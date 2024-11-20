from django.urls import path, include
from . import views


urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # 기본 회원가입 엔드포인트 대신 커스텀 뷰 사용
    path('dj-rest-auth/registration/', views.register),
    path('profile/<int:user_id>/', views.update_user_profile),
] 
