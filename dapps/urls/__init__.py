from django.conf.urls import url
from dapps.views import DAppsListView, DAppsDetailView, DappsFakeDetailView

urlpatterns = [
    url(r'^$', DAppsListView.as_view(), name='list'),
    url(r'^fakedetail\.htm$', DappsFakeDetailView.as_view(), name='detail_fake'),
    url(r'^(?P<slug>\d+)\.htm$', DAppsDetailView.as_view(), name='detail'),
]