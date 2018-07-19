from django.conf.urls import url

from applications.mp.views.api import (
    PeopleRankAPIView,
    PeopleDetailAPIView
)

urlpatterns = [
    url(r'^rank/$', PeopleRankAPIView.as_view(), name='rank'),
    # url(r'^search/?$')
    url(r'^dapps/(?P<login>[-\w]+)/?$', PeopleDetailAPIView.as_view(), name='detail'),
]