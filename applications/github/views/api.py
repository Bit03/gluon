import logging

from django.db.models import Count
from django.db.models.functions import TruncDate
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from applications.github.models import (
    People,
    Repository,
    RepositoryStats,
    Commit,
)
from applications.github.serializers import (
    PeopleSerializer,
    RepositorySerializer,
    RepositoryStatsSerializer,
    RepositoryCommitSerializer,
    RepositoryCommitStateSerializer,
)

logger = logging.getLogger('django')


# class OrganizationListAPIView(generics.ListCreateAPIView):
#     model = Organization
#     serializer_class = OrganizationSerializer
#     queryset = Organization.objects.all()
#     # pagination_class = StandardResultsSetPagination
#     ordering_fields = ('created_at',)
#
#
# class OrganizationDetailAPIView(generics.RetrieveUpdateAPIView):
#     serializer_class = OrganizationSerializer
#     queryset = Organization.objects.all()
#     lookup_field = 'name'


class PeopleListAPIView(generics.ListCreateAPIView):
    model = People
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    ordering_fields = ('created_at',)


class PeopleDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_field = 'login'


class RepositoryListAPIView(generics.ListCreateAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    ordering_fields = ('-updated_at',)


class UserRepositoryListAPIView(generics.ListAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    ordering_fields = ('-updated_at',)
    users = None

    def get_queryset(self):
        qs = self.queryset
        qs = qs.filter(author=self.users)
        return qs

    def get(self, request, *args, **kwargs):
        self.users = kwargs.pop('user', None)
        logging.info(self.users)
        return super(UserRepositoryListAPIView, self).get(request, *args, **kwargs)


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


class RepoStatsListAPIView(generics.CreateAPIView):
    queryset = RepositoryStats.objects.all()
    serializer_class = RepositoryStatsSerializer


class ReposCommitCreateAPIView(generics.CreateAPIView):
    queryset = Commit.objects.all()
    serializer_class = RepositoryCommitSerializer


class ReposCommitListAPIView(generics.ListAPIView):
    queryset = Commit.objects.all()
    serializer_class = RepositoryCommitStateSerializer

    def get_queryset(self):
        repo = Repository.objects.get(
            author=self.kwargs['user'],
            name=self.kwargs['repo'],
        )
        qs = self.queryset
        return qs.filter(repos=repo).annotate(date=TruncDate('commit_datetime'))\
            .values('date')\
            .annotate(commit_count=Count('id'))\
            .values('date', 'commit_count').order_by('-date')

