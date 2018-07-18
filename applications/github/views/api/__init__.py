import logging
from rest_framework import generics, filters
from haystack.query import SearchQuerySet

from applications.github.models import (
    People,
)
from applications.github.serializers import (
    PeopleSerializer,
    PeopleRankSerializer
)

logger = logging.getLogger('django')


class PeopleListAPIView(generics.ListCreateAPIView):
    model = People
    queryset = People.objects.filter(alive=True)
    serializer_class = PeopleSerializer
    ordering_fields = ('created_at',)


class PeopleDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = People.objects.filter(alive=True)
    serializer_class = PeopleSerializer
    lookup_field = 'login'


class PeopleRankAPIView(generics.ListAPIView):
    queryset = SearchQuerySet().models(People).all()
    serializer_class = PeopleRankSerializer
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = [
        "latest_7_day_commit",
        "latest_30_day_commit",
        "latest_90_day_commit",
    ]

