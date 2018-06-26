from django.conf.urls import url
from applications.github.views.api import PeopleListAPIView, PeopleDetailAPIView


urlpatterns = [
    url(r'^$', PeopleListAPIView.as_view(), name='list'),
    url(r'^(?P<login>[\-|\w]+)/?$', PeopleDetailAPIView.as_view(), name='detail'),
]