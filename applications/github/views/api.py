import logging
from rest_framework import generics
from applications.github.models import (
    People,
    Repository,
    RepositoryStats
)
from applications.github.serializers import (
    PeopleSerializer,
    RepositorySerializer,
    RepositoryStatsSerializer
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
        self.users = kwargs.pop('users', None)
        logging.info(self.users)
        return super(UserRepositoryListAPIView, self).get(request, *args, **kwargs)


class RepositoryDetailAPIView(generics.RetrieveAPIView):
    model = Repository
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    lookup_field = 'identified_code'


class RepoStatsListAPIView(generics.CreateAPIView):
    model = RepositoryStats
    queryset = RepositoryStats.objects.all()
    serializer_class = RepositoryStatsSerializer
