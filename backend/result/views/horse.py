from rest_framework import generics

from basic_info.models import Horse
from ..serializers.horse import HorseSerializer


class HorseResultView(generics.RetrieveAPIView):
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer
