from django.conf.urls import url
from github.views import (GitHubListView, ReposListView, ReposDetailView)


urlpatterns = [
    url(r'^$', GitHubListView.as_view(), name='list'),
    url(r'^(?P<author>\w+)/?$', ReposListView.as_view(), name='repos_list'),
    url(r'^repos/(?P<slug>\w+)/$', ReposDetailView.as_view(), name='repos_detail'),
]