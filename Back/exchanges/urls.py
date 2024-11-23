from django.urls import path
from . import views


urlpatterns = [
    path('save/', views.save_exchange),
    path('', views.exchange_list),
    path('clear/', views.clear_list),
]