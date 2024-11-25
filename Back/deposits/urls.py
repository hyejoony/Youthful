from django.urls import path
from . import views


urlpatterns = [
    path('save/', views.save_deposit),
    path('', views.deposit_product_list),
    path('recommend/', views.deposit_recommend_list),
    path('<int:product_id>/', views.deposit_product_detail),
    path('<int:product_id>/likes/', views.toggle_deposit_like),
]
