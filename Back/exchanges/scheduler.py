import schedule
import time
from django.utils import timezone


def job():
    # 한국 시간으로 저녁 11시에 실행
    if timezone.localtime().hour == 23:
        from .views import clear_list
        clear_list(None)  # None을 전달하는 대신 빈 request 객체를 만들어 전달하는 것이 더 좋을 수 있습니다


# 매일 실행
schedule.every().day.at("23:00").do(job)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)