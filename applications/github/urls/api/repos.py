from django.conf.urls import url
from applications.github.views.api import (
    RepositoryListAPIView,
    UserRepositoryListAPIView,
    RepositoryDetailAPIView,
    RepoStatsListAPIView
)

urlpatterns = [
    url(r'^$', RepositoryListAPIView.as_view(), name='list'),
    url(r'^(?P<users>)[-\w+]]/?$', UserRepositoryListAPIView.as_view(), name='users'),
    url(r'^stats/?$', RepoStatsListAPIView.as_view(), name='stats'),
    url(r'^(?P<identified_code>\w+)/?$', RepositoryDetailAPIView.as_view(), name='detail'),
]
