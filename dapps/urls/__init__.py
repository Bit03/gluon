from django.conf.urls import url
from dapps.views import DAppsListView, DAppsDetailView

urlpatterns = [
    url(r'^$', DAppsListView.as_view(), name='list'),
    url(r'^(?P<slug>\d+)\.htm$', DAppsDetailView.as_view(), name='detail'),
]