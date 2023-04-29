from rest_framework import generics
from rest_framework import exceptions

from ..models import Race
from ..serializers.race import RaceSerializer


class RaceView(generics.ListAPIView):
    serializer_class = RaceSerializer

    def get_queryset(self):

        query = self.request.query_params.get('race', None)
        if query is None:
            query = '201601010101'

        return Race.objects.filter(race_id=query)

    def filter_queryset(self, queryset):
        return queryset

