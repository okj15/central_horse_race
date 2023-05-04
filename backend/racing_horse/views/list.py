from rest_framework import generics

from ..models import RacingHorseResult
from ..serializers.list import RacingHorseResultSerializer

class RacingHorseResultsView(generics.ListAPIView):
    serializer_class = RacingHorseResultSerializer

    def get_queryset(self):
        race_id = self.request.query_params.get('race', None)
        if race_id is None:
            race_id = '201601010101'

        return RacingHorseResult.objects.filter(race__race_id=race_id)

    def filter_queryset(self, queryset):
        return queryset.order_by('rank')
