from django.conf.urls import url
from applications.github.views.api import (
    PeopleListAPIView,
    PeopleDetailAPIView,
    PeopleRankAPIView,
)


urlpatterns = [
    url(r'^$', PeopleListAPIView.as_view(), name='list'),
    url(r'^rank/?$', PeopleRankAPIView.as_view(), name='rank'),
    url(r'^(?P<login>[\-|\w]+)/?$', PeopleDetailAPIView.as_view(), name='detail'),
]