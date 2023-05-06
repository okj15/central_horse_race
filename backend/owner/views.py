from rest_framework import generics

from .models import OwnerResult
from .serializers import OwnerResultSerializer


class OwnerResultsView(generics.ListAPIView):
    queryset = OwnerResult.objects.all()
    serializer_class = OwnerResultSerializer

    def get_queryset(self):
        owner_id = self.request.query_params.get('owner', None)
        year = self.request.query_params.get('year', None)

        if owner_id is None:
            return []

        if not year:
            return OwnerResult.objects.filter(owner_id=owner_id)

        return OwnerResult.objects.filter(owner_id=owner_id, year=year)