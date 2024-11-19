from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import MapSerializers
from .models import Map


# GET - 지도 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def map_list(request):
    if request.method == 'GET':
        maps = get_list_or_404(Map)
        serializer = MapSerializers(maps, many=True)
        return Response(serializer.data)

