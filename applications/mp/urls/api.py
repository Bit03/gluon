from django.conf.urls import url

from applications.mp.views.api import (
    PeopleRankAPIView,
    PeopleSearchAPIView,
    PeopleDetailAPIView,
)

urlpatterns = [
    url(r'^rank/$', PeopleRankAPIView.as_view(), name='rank'),
    url(r'^search/?$', PeopleSearchAPIView.as_view(), name='search'),
    url(r'^dapps/(?P<login>[-\w]+)/?$', PeopleDetailAPIView.as_view(), name='detail'),
]