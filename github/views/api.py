from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

from github.models import (Organization, People, Repository)
from github.serializers import (OrganizationSerializer, PeopleSerializer, RepositorySerializer)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 1000


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
    pagination_class = StandardResultsSetPagination
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created_at',)


class RepositoryListAPIView(generics.ListCreateAPIView):
    model = Repository
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created_at',)
