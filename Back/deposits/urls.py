from django.urls import path
from . import views


urlpatterns = [
    path('save_deoposit/', views.save_deposit),
]
