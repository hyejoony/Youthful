from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    """
    커스텀 계정 어댑터

    allauth의 기본 계정 어댑터를 상속받아 사용자 등록 시 추가 필드를 처리합니다.
    """
    
    def save_user(self, request, user, form, commit=True):
        """
        사용자를 저장하는 메서드

        :param request: HTTP 요청 객체
        :param user: 새로 생성된 사용자 객체
        :param form: 사용자 등록 폼
        :param commit: 사용자를 데이터베이스에 즉시 저장할지 여부
        :return: 저장된 사용자 객체
        """
        
        # 기본 save_user 메서드를 호출하여 사용자 객체를 초기화
        user = super().save_user(request, user, form, False)
        data = form.cleaned_data  # 폼에서 전달된 유효한 데이터 가져오기

        # 추가 필드 저장
        user.birthyear = data.get('birthyear')  # 생년 저장
        user.income = data.get('income')  # 소득 저장
        user.career = data.get('career')  # 직업 저장
        user.region = data.get('region')  # 지역 저장
        user.condition1 = data.get('condition1', False)  # 조건1 저장 (기본값은 False)
        user.condition2 = data.get('condition2', False)  # 조건2 저장 (기본값은 False)

        # 프로필 이미지 저장
        if 'profile_img' in data:
            user.profile_img = data['profile_img']  # 프로필 이미지가 있는 경우 저장

        if commit:
            user.save()  # commit이 True일 경우 사용자 객체를 데이터베이스에 저장
        return user  # 최종적으로 저장된 사용자 객체 반환
