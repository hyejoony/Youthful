from django.urls import path
from . import views


urlpatterns = [
    path('save/', views.save_saving),
    path('', views.saving_product_list),
    path('<int:product_id>/', views.saving_product_detail),
    path('<int:product_id>/likes/', views.toggle_saving_like),
]
