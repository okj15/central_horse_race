from rest_framework import generics

from ..models import Master
from ..serializers.detail import RacingHorseSerializer


class RacingHorseDetailView(generics.RetrieveAPIView):
    queryset = Master.objects.all()
    serializer_class = RacingHorseSerializer
