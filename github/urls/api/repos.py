from django.conf.urls import url
from github.views.api import RepositoryListAPIView, RepoStatsListAPIView

urlpatterns = [
    url(r'^$', RepositoryListAPIView.as_view(), name='list'),
    url(r'^stats/?$', RepoStatsListAPIView.as_view(), name='stats')
]
