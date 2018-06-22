from rest_framework import generics
from rest_framework.filters import OrderingFilter
# from rest_framework.pagination import PageNumberPagination

from applications.github.models import (
    Organization,
    People,
    Repository,
    RepositoryStats
)
from applications.github.serializers import (
    OrganizationSerializer,
    PeopleSerializer,
    RepositorySerializer,
    RepositoryStatsSerializer
)


# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'size'
#     max_page_size = 1000


class OrganizationListAPIView(generics.ListCreateAPIView):
    model = Organization
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    # pagination_class = StandardResultsSetPagination
    ordering_fields = ('created_at',)


class OrganizationDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    lookup_field = 'name'


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
        return super(UserRepositoryListAPIView, self).get(request, *args, **kwargs)


class RepositoryDetailAPIView(generics.RetrieveAPIView):
    model = Repository
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    lookup_field = 'identified_code'


class RepoStatsListAPIView(generics.ListCreateAPIView):
    model = RepositoryStats
    queryset = RepositoryStats.objects.all()
    serializer_class = RepositoryStatsSerializer
