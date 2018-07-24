from django.conf.urls import url

from applications.mp.views.api import (
    PeopleRankAPIView,
    PeopleSearchAPIView,
    PeopleDetailAPIView,
    ReposCommitAPIView
)

urlpatterns = [
    url(r'^rank/$', PeopleRankAPIView.as_view(), name='rank'),
    url(r'^search/?$', PeopleSearchAPIView.as_view(), name='search'),
    url(r'^dapps/(?P<login>[\-|\w]+)/?$', PeopleDetailAPIView.as_view(), name='detail'),
    url(r'^github/(?P<login>[\-|\w]+)/commit/?$', ReposCommitAPIView.as_view(), name='commit'),
]