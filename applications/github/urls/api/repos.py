from django.conf.urls import url
from applications.github.views.api import (
    RepositoryListAPIView,
    UserRepositoryListAPIView,
    UserRepositoryCommitListAPIView,
    RepositoryCheckAPIView,
    RepositoryDetailAPIView,
    RepoStatsCreateAPIView,
    RepoStatsListAPIView,
    ReposCommitCreateAPIView,
    ReposCommitListAPIView,
)

urlpatterns = [
    url(r'^$', RepositoryListAPIView.as_view(), name='list'),
    url(r'^stats/?$', RepoStatsCreateAPIView.as_view(), name='stats'),
    url(r'^commit/?$', ReposCommitCreateAPIView.as_view(), name='commit'),
    url(r'^check/(?P<identified_code>\w+)/?$', RepositoryCheckAPIView.as_view(), name='check'),

    url(r'^(?P<user>[\-|\w]+)/?$', UserRepositoryListAPIView.as_view(), name='users'),
    url(r'^(?P<user>[\-|\w]+)/commit/?$', UserRepositoryCommitListAPIView.as_view(), name='users_commit'),

    url(r'^(?P<user>[\-|\w]+)/(?P<repo>[\-|\.|\w]+)/?$', RepositoryDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<user>[\-|\w]+)/(?P<repo>[\-|\.|\w]+)/state/?$',
        RepoStatsListAPIView.as_view(),
        name='repos_state'),
    url(r'^(?P<user>[\-|\w]+)/(?P<repo>[\-|\.|\w]+)/commit/?$',
        ReposCommitListAPIView.as_view(),
        name='repos_commit'),
]
