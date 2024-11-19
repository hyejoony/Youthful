from rest_framework import serializers
from .models import Map

# 주변 은행 검색 시리얼라이즈
class MapSerializers(serializers.ModelSerializer):

    class Meta:
        model = Map
        fields = '__all__'