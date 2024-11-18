from rest_framework import serializers
from .models import Community, CommunityComment
from django.contrib.auth import get_user_model

User = get_user_model()

