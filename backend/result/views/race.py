from rest_framework import generics

from ..models import Race
from ..serializers.race import RaceResultSerializer, RaceInfoSerializer


class RaceInfoView(generics.ListAPIView):
    serializer_class = RaceInfoSerializer

    def get_queryset(self):
        query = self.request.query_params.get('race', None)
        if query is None:
            query = '201601010101'

        return [Race.objects.filter(race_id=query).first()]


class RaceResultView(generics.ListAPIView):
    serializer_class = RaceResultSerializer

    def get_queryset(self):
        query = self.request.query_params.get('race', None)
        if query is None:
            query = '201601010101'

        return Race.objects.filter(race_id=query)

    def filter_queryset(self, queryset):
        return queryset
