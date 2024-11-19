from django.urls import path
from . import views


urlpatterns = [
    path('', views.community_list),
    path('<int:community_id>/', views.community_detail),
    path('<int:community_id>/comments/', views.comment_create),
    path('<int:community_id>/comments/<int:comment_id>/', views.comment_detail),
]
