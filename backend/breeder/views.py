from rest_framework import generics

from .models import BreederResult
from .serializers import BreederResultSerializer


class BreederResultsView(generics.ListAPIView):
    queryset = BreederResult.objects.all()
    serializer_class = BreederResultSerializer

    def get_queryset(self):
        breeder_id = self.request.query_params.get('breeder', None)
        year = self.request.query_params.get('year', None)

        if breeder_id is None:
            return []

        if not year:
            return BreederResult.objects.filter(breeder_id=breeder_id)

        return BreederResult.objects.filter(breeder_id=breeder_id, year=year)
