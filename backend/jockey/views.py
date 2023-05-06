from rest_framework import generics

from .models import JockeyResult
from .serializers import JockeyResultSerializer


from racing_horse.models import RacingHorseResult

class JockeyResultsView(generics.ListAPIView):
    queryset = JockeyResult.objects.all()
    serializer_class = JockeyResultSerializer

    def get_queryset(self):
        race_id = self.request.query_params.get('race', None)

        if race_id is None:
            return []

        race = RacingHorseResult.objects.filter(race__race_id=race_id)
        jockey_ids = [r.jockey_id for r in race]
        year = race_id[:4]


        return JockeyResult.objects.filter(jockey_id__in=jockey_ids, year=year)
