from django.conf.urls import url
from github.views import GitHubListView, ReposListView


urlpatterns = [
    url(r'^$', GitHubListView.as_view(), name='list'),
    url(r'^repos/(?P<author>\w+)/?$', ReposListView.as_view(), name='repos_list'),
]