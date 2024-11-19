from django.urls import path
from . import views


urlpatterns = [
    path('save/', views.save_subsidy),
    path('', views.subsidy_list),
    path('<int:subsidy_id>/', views.subsidy_detail),
    path('<int:subsidy_id>/likes/', views.toggle_subsidy_like),
    path('<int:subsidy_id>/comments/', views.comment_create),
    path('<int:subsidy_id>/comments/<int:comment_id>/', views.comment_detail),
]
