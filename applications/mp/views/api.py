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
    queryset = SearchQuerySet().models(People)
    serializer_class = PeopleRankSerializer

    def get_queryset(self):
        qs = self.queryset
        return qs.filter(auto_login=self.request.GET.get('q', None))


class PeopleDetailAPIView(generics.RetrieveAPIView):
    queryset = SearchQuerySet().models(People).all()
    serializer_class = PeopleRankDetailSerializer
    lookup_field = 'login'

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        qs = self.get_queryset().filter(**filter_kwargs)
        return qs[0]

