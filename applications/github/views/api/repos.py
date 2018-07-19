import logging
import pandas as pd
from datetime import datetime, timedelta
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate
from haystack.query import SearchQuerySet
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from applications.utils.renderers import (
    CommitChartRenderer,
    StatChartRenderer
)

from applications.github.models import (
    Repository,
    RepositoryStats,
    Commit,
)
from applications.github.serializers import (
    RepositorySerializer,
    RepositoryStatsSerializer,
    RepositoryStateChartSerializer,
    RepositoryCommitSerializer,
    RepositoryCommitStateSerializer,
)

logger = logging.getLogger('django')


class RepositoryListAPIView(generics.ListCreateAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    ordering_fields = ('-updated_at',)


class UserRepositoryListAPIView(generics.ListAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    ordering_fields = ('-updated_at',)

    def get_queryset(self):
        qs = self.queryset
        qs = qs.filter(author=self.kwargs.pop('user'))
        return qs


class UserRepositoryCommitListAPIView(generics.ListAPIView):
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


class UserRepositoryStateListAPIView(generics.ListAPIView):
    queryset = RepositoryStats.objects.all()
    serializer_class = RepositoryStateChartSerializer
    pagination_class = None
    renderer_classes = (StatChartRenderer,)

    @property
    def start(self):
        _before = self.request.GET.get('before', 30)
        if not isinstance(_before, int):
            _before = int(_before)
        _start = datetime.now() - timedelta(days=_before)
        return _start

    def process_dataframe(self, df):
        ret = pd.DataFrame(
            {
                "date": df.sort_index().index.tolist(),
                "watch": df.sort_index().watch_sum.diff().fillna(0).tolist(),
                "star": df.sort_index().star_sum.diff().fillna(0).tolist(),
                "fork": df.sort_index().fork_sum.diff().fillna(0).tolist(),
            },

        )
        return ret.itertuples(index=True)

    def get_queryset(self):
        qs = self.queryset
        repo = Repository.objects.filter(
            author=self.kwargs['user'],
        ).values_list('pk', flat=True)
        qs = qs.filter(repos__in=repo) \
            .filter(date__range=(self.start, datetime.now())) \
            .values('date') \
            .annotate(star_sum=Sum('star'), watch_sum=Sum('watch'), fork_sum=Sum('fork')) \
            .values('watch_sum', 'star_sum', 'fork_sum', 'date') \
            .order_by("date")
        logger.info(qs.query)
        df = qs.to_dataframe(index='date')
        return self.process_dataframe(df=df)


class RepositoryCheckAPIView(generics.RetrieveAPIView):
    model = Repository
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    lookup_field = 'identified_code'


class RepositoryDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        filter_kwargs = {
            "author": self.kwargs['user'],
            "name": self.kwargs['repo']
        }
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj


class RepoStatsCreateAPIView(generics.CreateAPIView):
    queryset = RepositoryStats.objects.all()
    serializer_class = RepositoryStatsSerializer


class RepoStatsListAPIView(generics.ListAPIView):
    queryset = RepositoryStats.objects.all()
    serializer_class = RepositoryStateChartSerializer
    pagination_class = None
    renderer_classes = (StatChartRenderer,)

    def process_dataframe(self, df):
        ret = pd.DataFrame(
            {
                "date": df.sort_index().index.tolist(),
                "watch": df.sort_index().watch.diff().fillna(0).tolist(),
                "star": df.sort_index().star.diff().fillna(0).tolist(),
                "fork": df.sort_index().fork.diff().fillna(0).tolist(),
            },

        )
        return ret.itertuples(index=True)

    def get_queryset(self):
        qs = self.queryset
        repo = Repository.objects.get(
            author=self.kwargs['user'],
            name=self.kwargs['repo'],
        )
        df = qs.filter(repos=repo).order_by("date").to_dataframe(index='date')

        return self.process_dataframe(df=df)


class ReposCommitCreateAPIView(generics.CreateAPIView):
    queryset = Commit.objects.all()
    serializer_class = RepositoryCommitSerializer

    # def crea


class ReposCommitListAPIView(generics.ListAPIView):
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
        repo = Repository.objects.get(
            author=self.kwargs['user'],
            name=self.kwargs['repo'],
        )
        qs = self.queryset
        return qs.filter(repos=repo).filter(commit_datetime__range=(self.start, datetime.now())) \
            .annotate(date=TruncDate('commit_datetime')) \
            .values('date') \
            .annotate(commit_count=Count('id')) \
            .values('date', 'commit_count').order_by('-date')
