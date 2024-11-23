from django.apps import AppConfig


class ExchangesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exchanges'

# 서버 시작 시 스케줄러를 실행
import threading

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exchanges'

    def ready(self):
        from .scheduler import run_scheduler
        scheduler_thread = threading.Thread(target=run_scheduler)
        scheduler_thread.start()