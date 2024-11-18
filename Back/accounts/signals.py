from django.db.models.signals import post_save  
from django.dispatch import receiver  
from rest_framework.authtoken.models import Token  
from django.conf import settings  

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    사용자 인스턴스가 생성될 때마다 호출되는 신호 처리기

    :param sender: 신호를 보낸 모델 클래스 (여기서는 사용자 모델)
    :param instance: 생성된 사용자 인스턴스
    :param created: 인스턴스가 새로 생성되었는지 여부
    :param kwargs: 추가적인 키워드 인자
    """
    if created:
        # 사용자가 새로 생성된 경우, 해당 사용자에 대한 인증 토큰을 생성
        Token.objects.create(user=instance)
