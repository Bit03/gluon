from haystack.query import SearchQuerySet
from rest_framework import generics, filters

from applications.github.models import People
from applications.mp.serializers import PeopleRankSerializer, PeopleRankDetailSerializer


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


class PeopleSearchAPIView(generics.ListAPIView):
    pass


class PeopleDetailAPIView(generics.RetrieveAPIView):
    queryset = SearchQuerySet().models(People).all()
    serializer_class = PeopleRankDetailSerializer
    lookup_field = 'login'
