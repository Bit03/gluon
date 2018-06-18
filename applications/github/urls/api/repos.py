from django.conf.urls import url
from github.views.api import (RepositoryListAPIView,
                              RepositoryDetailAPIView,
                              RepoStatsListAPIView)

urlpatterns = [
    url(r'^$', RepositoryListAPIView.as_view(), name='list'),
    url(r'^stats/?$', RepoStatsListAPIView.as_view(), name='stats'),
    url(r'^(?P<identified_code>\w+)/?$', RepositoryDetailAPIView.as_view(), name='detail'),
]
