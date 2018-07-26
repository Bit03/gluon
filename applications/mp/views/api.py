from datetime import datetime, timedelta

from django.db.models import Count
from django.db.models.functions import TruncDate
from haystack.query import SearchQuerySet
from rest_framework import generics, filters

from applications.github.models import People, Commit, Repository
from applications.github.serializers import RepositoryCommitStateSerializer
from applications.mp.serializers import PeopleRankSerializer, PeopleRankDetailSerializer
from applications.utils.renderers import CommitChartRenderer


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


# class PeopleAutoCompleteAPIView(generics.ListAPIView):
#     queryset = SearchQuerySet().models(People)
#
#     def get_queryset(self):
#         qs = self.queryset
#         return qs.autocomplete(auto_login=self.request.GET.get('q', None))


class PeopleDetailAPIView(generics.RetrieveAPIView):
    queryset = SearchQuerySet().models(People).all()
    serializer_class = PeopleRankDetailSerializer
    lookup_field = 'login'

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        qs = self.get_queryset().filter(**filter_kwargs)
        return qs[0]


class ReposCommitAPIView(generics.ListAPIView):
    queryset = Commit.objects.all()
    serializer_class = RepositoryCommitStateSerializer
    pagination_class = None

    renderer_classes = (CommitChartRenderer,)

    @property
    def start(self):
        _before = self.request.GET.get('before', 30)
        if not isinstance(_before, int):
            _before = int(_before)
        _start = datetime.now() - timedelta(days=_before)
        return _start

    def get_queryset(self):
        repos = Repository.objects.filter(
            author=self.kwargs['user'],
        ).values_list('pk', flat=True)
        qs = self.queryset
        return qs.filter(repos_id__in=repos).filter(commit_datetime__range=(self.start, datetime.now())) \
            .annotate(date=TruncDate('commit_datetime')) \
            .values('date') \
            .annotate(commit_count=Count('id')) \
            .values('date', 'commit_count').order_by('-date')
