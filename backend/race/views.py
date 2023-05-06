from rest_framework import generics

from .models import Race
from .serializers import RaceSerializer


class RaceView(generics.ListAPIView):
    serializer_class = RaceSerializer

    def get_queryset(self):
        query = self.request.query_params.get('race', None)
        if query is None:
            return []

        return [Race.objects.filter(race_id=query).first()]