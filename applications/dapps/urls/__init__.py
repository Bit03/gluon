from django.conf.urls import url
from applications.dapps.views import (
    DAppSearchListView,
    DAppsListView,
    DAppsDetailView
)

urlpatterns = [
    url(r'^$', DAppsListView.as_view(), name='list'),
    url(r'^search/?$', DAppSearchListView.as_view(), name='search'),
    url(r'^(?P<slug>\d+)\.htm$', DAppsDetailView.as_view(), name='detail'),
]
