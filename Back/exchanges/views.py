from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ExchangeSerializers
from .models import Exchange


# GET - 환율 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def exchange_list(request):
    if request.method == 'GET':
        exchanges = get_list_or_404(Exchange)
        serializer = ExchangeSerializers(exchanges, many=True)
        return Response(serializer.data)

