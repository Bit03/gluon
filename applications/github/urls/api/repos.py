from django.conf.urls import url
from applications.github.views.api import (
    RepositoryListAPIView,
    UserRepositoryListAPIView,
    RepositoryCheckAPIView,
    RepositoryDetailAPIView,
    RepoStatsListAPIView,
    ReposCommitCreateAPIView,
    ReposCommitListAPIView,
)

urlpatterns = [
    url(r'^$', RepositoryListAPIView.as_view(), name='list'),
    url(r'^stats/?$', RepoStatsListAPIView.as_view(), name='stats'),
    url(r'^commit/?$', ReposCommitCreateAPIView.as_view(), name='commit'),
    url(r'^check/(?P<identified_code>\w+)/?$', RepositoryCheckAPIView.as_view(), name='check'),

    url(r'^(?P<user>[\-|\w]+)/?$', UserRepositoryListAPIView.as_view(), name='users'),
    url(r'^(?P<user>[\-|\w]+)/(?P<repo>[\-|\.|\w]+)/?$', RepositoryDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<user>[\-|\w]+)/(?P<repo>[\-|\.|\w]+)/commit/?$', ReposCommitListAPIView.as_view(), name='list_commit'),
]
