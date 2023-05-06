from rest_framework import generics

from .models import TrainerResult
from .serializers import TrainerResultSerializer


class TrainerResultsView(generics.ListAPIView):
    queryset = TrainerResult.objects.all()
    serializer_class = TrainerResultSerializer

    def get_queryset(self):
        trainer_id = self.request.query_params.get('trainer', None)
        year = self.request.query_params.get('year', None)

        if trainer_id is None:
            return []

        if not year:
            return TrainerResult.objects.filter(trainer_id=trainer_id)

        return TrainerResult.objects.filter(trainer_id=trainer_id, year=year)
